import socket

class client_pastie(object):
    def __init__(self):
        self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.port = 8887
        pass

    def _req_msg(self, method, data):
        if method == "GET":
            msg = "{} /{}\r\n".format(method, data)
        elif method == "PUT":
            msg = "{} {}\r\n".format(method, data)
        return msg

    def get_message(self, url):
        self.sk.connect((self.host, self.port))
        self.sk.send(self._req_msg("GET", url))
        data = self.sk.recv(200)
        return data

    def put_message(self, data):
        self.sk.connect((self.host, self.port))
        self.sk.send(self._req_msg("PUT", data))
        data = self.sk.recv(200)
        return data

    def edit_message(self, url):
        pass

    def remove_message(self, url):
        pass
