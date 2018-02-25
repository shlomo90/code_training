#!/usr/bin/python
# -*- encoding: utf-8 -*-

'''
This is the simple python code for get the key value from website.

Author : 임재환
'''


import sys
import requests
import time
import re


def get_pask_key(serial, hostname='switch', mute=False):

    """ Return the pas-k key value

    doctest
    >>> get_pask_key('something') #doctest: +ELLIPSIS
    ...
    """

    now = time.gmtime()
    year = now.tm_year
    mon = now.tm_mon
    mday = now.tm_mday
    # date = '{}{}{0:02d}'.format(str(year), str(mon), str(mday))
    date = "%d%02d%02d" % (year, mon, mday)
    if mute is False:
        print date
    uri = "http://keygen.piolink.com/cgi-bin/startshell.cgi"

    """ These must need to post the request to uri. """
    payload = {'hostname': hostname,
               'serial': serial,
               'date': date
               }

    r = requests.post(uri, data=payload)
    cnt = r.content

    cnt_list = cnt.split('\n')

    for line in cnt_list:
        line = line.strip()
        line = line.replace('\t', '')
        if line.find('id="result"') >= 0:
            pattern = re.compile('value="(.*)"')
            result = pattern.search(line)
            if result:
                key = result.group(1)
    return key


if __name__ == "__main__":

    """ You must input the serial number.
        hostname is optional. default is 'switch' """

    if len(sys.argv) == 3:
        key = get_pask_key(sys.argv[1], sys.argv[2])
    else:
        key = get_pask_key(sys.argv[1])

    print(key)
