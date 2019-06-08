import pymysql
import time
import hashlib

DB_SERVER_NAME = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'pastie'
DB_CHARSET = 'utf8'
DB_CURSOR_TYPE = pymysql.cursors.DictCursor
DB_TABLE = 'message'


class pastie_db(object):

    def __init__(self, user=DB_USER, passwd=DB_PASSWORD,
                 name=DB_NAME, charset=DB_CHARSET):

        self.user = user
        self.passwd = passwd
        self.name = name
        self.charset = charset
        self.conn = None

    def connect(self, user=DB_USER, password=DB_PASSWORD):
        conn = None
        try:
            conn = pymysql.connect(host=DB_SERVER_NAME, user=user,
                                   password=password, charset=self.charset,
                                   cursorclass=DB_CURSOR_TYPE)
            self.conn = conn
            #check database exist?
            cur_obj = conn.cursor()
            query = "show databases"
            cur_obj.execute(query)
            db_list = [ x['Database'] for x in cur_obj.fetchall() ]

            if DB_NAME in db_list:
                cur_obj.execute("use pastie")
            else:
                query = "create database {}".format(DB_NAME)
                cur_obj.execute(query)
                cur_obj.execute("use pastie")

            #check table "message"
            cur_obj.execute("show tables")
            table_list = [ x['Tables_in_pastie'] for x in cur_obj.fetchall() ]
            if DB_TABLE in table_list:
                pass
            else:
                query = ("create table {} "
                         "(id INT(11) NOT NULL AUTO_INCREMENT, "
                         "hash varchar(100), "
                         "msg varchar(200), CONSTRAINT pk_message "
                         "PRIMARY KEY(id, hash))".format(DB_TABLE))
                cur_obj.execute(query)
            print "good"
        except Exception as e:
            print("Connection Fail! {}".format(e))

        return conn

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()

    def insert(self, data):
        h = hashlib.md5(str(time.time()) + data).hexdigest()
        try:
            cur_obj = self.conn.cursor()
            query = "insert into {} (hash, msg) values ('{}', '{}')".format(
                    "message", h, data)
            print "query : {}".format(query)
            cur_obj.execute(query)
            self.conn.commit()
        except Exception as e:
            print("Insert Data Fail! {}".format(e))
            return 'nok', ''
        
        return 'ok', h

    def search(self, key):
        if self.conn is None:
            return None

        key = key.strip()
        cur_obj = self.conn.cursor()
        search_query = ("SELECT msg FROM {} ".format(DB_TABLE)
                        + "WHERE hash = '{}'".format(key))
        print "query : {}".format(search_query)
        cur_obj.execute(search_query)
        msg = cur_obj.fetchall()
        if msg:
            return msg[0]["msg"]
        else:
            return ''

'''
dbServerName    = 'localhost'
dbUser          = 'root'
dbPassword      = 'INMJinmj3020!'
dbName          = 'pastie'
charSet         = 'utf8'
cursorType      = pymysql.cursors.DictCursor

conn = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                       charset=charSet, cursorclass=cursorType)

try:
    curObject = conn.cursor()
    sqlStatement = 'CREATE DATABASE ' + dbName
    curObject.execute(sqlStatement)

    sqlQuery = 'SHOW DATABASES'

    curObject.execute(sqlQuery)

    databaseList = curObject.fetchall()

    for database in databaseList:
        print(database)

except Exception as e:
    print("Exception occured:{}".format(e))

finally:
    conn.close()
'''
