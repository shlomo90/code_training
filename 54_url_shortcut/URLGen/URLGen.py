#-*- encoding:utf-8 -*-
from DB.DB import CSVDB

class InvalidURL(BaseException):
    pass

class ShortCutService(object):
    ''' Do the short cut service for Long URL
    '''
    def __init__(self, url=None, db=None):
        self.url = url
        self.db = CSVDB('test') if db is None else db

        ''' It's Default '''
        self.max_domain = 8
        self.max_uri = 8

    def is_long_url(self):
        max_domain = self.max_domain
        max_uri = self.max_uri
        if max_domain <= self.url.get_domain():
            return True
        elif max_uri <= self.url.get_uri():
            return True
        else:
            return False

    def find_url(self, url, opt='long_url'):
        return self.db.find(url, opt)

    def get_shorten_url(self, url):
        # initiating and load
        elem = self.find_url(url)
        if elem:
            shorten_url = elem['short_url']
            elem['count'] += 1
            self.update(url, elem, opt="long_url")
            return shorten_url
        else:
            return None

    def push_url(self, long_url, short_url, expire=0):
        self.db.add(long_url, short_url, expire)

    def update(self, key, target, opt="long_url"):
        data = self.db.data
        for elem in data:
            if key in elem[opt]:
                #XXX: Need to arrange code.
                elem['long_url'] = target['long_url']
                elem['short_url'] = target['short_url']
                elem['count'] = target['count']
                elem['expire'] = target['expire']
        self.db.update()

    def generate_shorten(self):
        domain = self.url.get_domain()
        uri = self.url.get_uri()
        domain = domain[:self.max_domain]
        uri = uri[:self.max_uri]
        full_url = self.url.combine(domain, uri)
        self.push_url(self.url.get_url(), full_url, expire=10)
        return full_url


class URL(object):
    def __init__(self, url=''):
        self.validate(url)
        self.url = url
        self.scheme, self.domain, self.uri =  self.parse(self.url)

    def combine(self, domain, uri):
        return self.scheme + "://" + domain + uri

    def get_url(self):
        return self.url

    def get_domain(self):
        return self.domain

    def get_uri(self):
        return self.uri

    def parse(self, url_string):
        # We just treat url like http(s)://~~~
        idx = url_string.index("://")
        scheme = url_string[:idx]
        base = filter(None, url_string[idx+3:].split('/', 1))
        domain = base[0]
        uri = '/'
        if len(base) == 2:
            uri = '/' + base[1]
        return (url_string[:idx], domain, uri)

    def validate(self, url_string):
        target = url_string
        target = target.strip("")

        # white space check
        if " " in target:
            raise InvalidURL

        # hiarachy check
        try:
            idx = target.index('://')
        except BaseException as e:
            raise InvalidURL
       
        # scheme check (Target should be http or https)
        scheme = target[:idx]
        if scheme not in ['http', 'https']:
            raise InvalidURL

        #domain check
        if len(target[idx+3:]) == 0:
            raise InvalidURL

        return True
