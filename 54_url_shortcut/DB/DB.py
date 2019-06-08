#-*- encoding:utf-8 -*-

# all about DB
# Constraints
#  1. DB is not implemented, so, We just use CSV file.

PATH = './db.csv'

class SingletonMetaClass(type):
    def __init__(cls, name, bases, dict):
        #print "cls {}".format(cls)
        #print "name {}".format(name)
        #print "base {}".format(bases)
        #print "dict {}".format(dict)
        super(SingletonMetaClass, cls).__init__(name, bases, dict)
        original_new = cls.__new__

        def my_new(cls, *args, **kwargs):
            if cls.instance == None:
                cls.instance = original_new(cls, *args, **kwargs)
            return cls.instance

        cls.instance = None
        cls.__new__ = staticmethod(my_new)

class CSVDB(object):
    __metaclass__ = SingletonMetaClass

    def __init__(self, val):
        self.data = None
        self.val = val
        #print "self {}".format(self)
        self.path = './db.csv'
        self.delim = ','


    def __str__(self):
        return `self` + self.val

    def load(self):
        data = []
        with open(PATH, 'r') as f:
            for line in f.readlines():
                line.strip()
                long_url, short_url, cnt, exp = line.split(',')

                data.append({'long_url': long_url.strip(),
                             'short_url': short_url.strip(),
                             'count' : int(cnt.strip()),
                             'expire' : int(exp.strip()),
                             })
        self.data = data
        return data
        
    def update(self):
        self.data
        with open(PATH, 'w') as f:
            for line in self.data:
                if line['count'] >= line['expire']:
                    continue
                line_msg = '{long_url},{short_url},{count},{expire}\n'
                f.write(line_msg.format(**line))

    def add(self, long_url, short_url, expire):
        #XXX: Does it need?
        self.update()
        count = 0

        with open(PATH, 'a') as f:
            line_msg = '{},{},{},{}\n'.format(long_url, short_url, count, expire)
            f.write(line_msg)

    def find(self, url, opt="long_url"):
        data = self.load()
        for elem in data:
            if url == elem[opt]:
                return elem
        return None
