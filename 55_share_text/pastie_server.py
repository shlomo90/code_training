#-*- encoding:utf-8 -*-
import socket
from pastie_db import pastie_db


#HOST = "124.5.188.23"
HOST = "0.0.0.0"
PORT = 8887
METHOD_LIST = ['GET', 'PUT']

class ServerError(BaseException):
    pass


class PastieServer(object):
    def __init__(self, host=HOST, port=PORT, db=pastie_db()):
        self.db = db
        self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.sk.bind((host, port))
        self.sk.listen(5)


    def _connect_db(self):
        user = raw_input("DB user: ")
        if user.strip() == '':
            raise ValueError("invalid input user")
        passwd = raw_input("DB {} password: ".format(user))
        if passwd.strip() == '':
            raise ValueError("Empty Password")

        if self.db.connect(user=user, password=passwd) is None:
            raise ServerError("DB Connection Error")


    def run(self):
        self._connect_db()

        while True:
            client_sk, addr = self.sk.accept()   # blocking
            data = client_sk.recv(100) # buff size
            try:
                meth, data = self._parse_request(data)
                if meth == "GET":
                    data = data[1:]
            except BaseException as e:
                print "Invalid Request message. Ignored {}".format(e)
                continue

            if meth == "GET":
                ret = self.db.search(data)
                if ret == '':
                    client_sk.send('nothing')
                    print "server: get nothing"
                else:
                    print "server: {}".format(ret)
                    client_sk.send(ret)
            elif meth == "PUT":
                ret, h = self.db.insert(data)
                if ret == "ok":
                    print "server: ok"
                    client_sk.send(ret + ' {}'.format(h))
                else:
                    client_sk.send('nok')
                    print "server: put fail"

    def _parse_request(self, data):
        ''' Client request message format
        "<METHOD> /<URL>"
        GET /jaklfjkleajwfk
        PUT message
        '''
        try:
            method, data = data.split(' ', 1)
        except ValueError as e:
            raise ValueError("Invalid Data Format: {}".format(data))
        
        if method not in METHOD_LIST:
            raise ValueError("Invalid Method Format: {}".format(method))

        if method == "GET":
            url = data
            if len(url) == 0 or url[0] != '/':
                raise ValueError("Invalid URL Format: {}".format(url))
            return method, url
        else:
            msg = data
            return method, msg


if __name__ == "__main__":
    
    server = PastieServer()
    server.run()
