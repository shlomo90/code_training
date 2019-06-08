#-*- encoding: utf-8 -*-

'''
JSON Server.

We will descript about My server. The code related to Server is written here.
We only support 'JSON' and Clients must use an application/json of the content type.



'''

import socket
import datetime
import httplib
import json


class TimeServer(object):
    HOST = ''
    PORT = 8080
    MAX_PACKET = 32768

    def __init__(self, host=None, port=None):
        self.HOST = host if host else self.HOST
        self.port = port if port else self.PORT
        self.sock = None


    def init(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as msg:
            print("errmsg : {}".format(msg))
            self.sock = None
            return -1

        return self.sock


    def run(self):
        '''
        open current IP(dynamic or static) and port 80(or option user put).
        We use TCP/IP connection.
        If the Socket is successfully opened. This function will print IP, Port,
        extra Information for client connecting to this server.
        '''

        s = self.sock
        try:
            s.bind((self.HOST, self.PORT))
        except socket.error, msg:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        lis_ret = s.listen(1)


        print("server is now running!")
        while True:
            conn, addr = s.accept()
            # log need to be appended

            data = self.normalize_line_encodings(self._recv_all(conn))

            request_head, request_body = data.split('\n\n', 1)
            request_head = request_head.splitlines()

            req_head = dict(x.split(': ', 1) for x in request_head[1:])
            if self._has_header(req_head,
                              "Content-type",
                              "application/json"):
                send_data = self._normal_response_msg()
            else:
                #TODO: send error message
                send_data = self._error_response_msg()

            conn.send('\n'.join(send_data))
            conn.close()


    def stop(self):
        self.sock.close()


    def _recv_all(self, sock):
        prev_timeout = sock.gettimeout()
        try:
            sock.settimeout(0.01)

            rdata = []
            while True:
                try:
                    rdata.append(sock.recv(self.MAX_PACKET))
                except socket.timeout:
                    return ''.join(rdata)

            # unreachable
        finally:
            sock.settimeout(prev_timeout)


    def _normal_response_msg(self):
        r'''This function makes response data message.
        the response data has a current time as JSON string.
        return type is list type in python, and the caller must join this list as
        whole string.''' 

        r''' Normal usually code data of response.
        HTTP/1.1 200 OK
        Date: Sat, 19 May 2007 13:49:37 GMT
        Server: IBM_HTTP_SERVER/1.3.26.2 Apache/1.3.26 (Unix)
        Set-Cookie: tracking=tI8rk7joMx44S2Uu85nSWc
        Pragma: no-cache
        Expires: Thu, 01 Jan 1970 00:00:00 GMT
        Content-Type: text/html;charset=ISO-8859-1
        Content-Language: en-US
        Content-Length: 24246
        '''

        http_version = "HTTP/1.1"
        http_status = "200"
        http_result = "OK"

        # body data
        dict_ret = {}
        dict_ret["currentTime"] = self.get_current_time()
        json_data = json.dumps(dict_ret)

        # make msg
        msg = []
        msg.append("{} {} {}".format(http_version, http_status, http_result))

        response_headers = {
            'Content-Type': 'application/json; encoding=utf8',
            'Content-Length': len(json_data)+2,
            'Server': 'Lim_Jae_hwan_sever',
            'Connection': 'close',
        }
        response_headers_raw = ''.join('%s: %s\n' % (k, v) for k, v in \
                                                response_headers.iteritems())
        msg.append(response_headers_raw)
        msg.append("\n")
        msg.append(json_data)

        return msg


    def _error_response_msg(self):
        http_version = "HTTP/1.1"
        http_status = "503"
        http_result = "Service Temporarily Unavailable"

        msg = []
        msg.append("{} {} {}".format(http_version, http_status, http_result))

        # body data
        response_data = "Sorry..."

        response_headers = {
            'Content-Type': 'application/json; encoding=utf8',
            'Content-Length': len(response_data),
            'Server': 'Lim_Jae_hwan_sever',
            'Connection': 'close',
        }
        response_headers_raw = ''.join('%s: %s\n' % (k, v) for k, v in \
                                                response_headers.iteritems())
        msg.append(response_headers_raw)
        msg.append('\n')
        msg.append(response_data)
        return msg


    def normalize_line_encodings(self, s):
        r''' I got this code from
        'https://stackoverflow.com/questions/10114224/how-to-properly-send-http-
        response-with-python-using-socket-library-only'
        '''

        r'''Convert string containing various line endings like \n, \r or \r\n,
        to uniform \n.'''

        return ''.join((line + '\n') for line in s.splitlines())

    def get_current_time(self):
        now = datetime.datetime.now()
        return str(now)

    def _has_header(self, req_head, key, value):
        for key, value in req_head.iteritems():
            if (key.find(key) != -1 \
                    and value.find(value) != -1):
                return True

        return False


if __name__ == "__main__":
    t = TimeServer()
    t.init()
    t.run()
