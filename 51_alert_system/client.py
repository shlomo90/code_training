import httplib
import json


class Client(object):
    HOST = '127.0.0.1'      # loop back. The remote host
    PORT = 8080              # The same port as used by the server

    def __init__(self):
        pass


    def request_time(self):
        method = "GET"
        path = "/"
        param = ""
        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain"}

        conn = httplib.HTTPConnection(self.HOST, str(self.PORT))
        conn.request(method, path, param, headers)

        recv = conn.getresponse()
        if "200" in str(recv.status):
            text = recv.read(1024)
            data = json.loads(text)
            time = data["currentTime"]

            print("The current time is {}".format(time))
        else:
            print recv.read(1024)


if __name__ == "__main__":
    c = Client()
    c.request_time()
