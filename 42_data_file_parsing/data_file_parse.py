# -*- encoding: utf-8 -*-

import sys
import csv
import time

'''
다음의 내용이 들어 있는 파일을 읽는 프로그램을 작성하라.


Ling,mai,55900
Johnson,Jim,56500
Jones,Aaron,46000
Jones,Chris,34500
Swift,Geoffrey,14200
Xiong,Fong,65000
Zarneck,Sabrina,51500

이렇게 읽은 데이터를 처리하여 다음의 출력 예와 같이 정렬된 표 형식으로
출력해보자.

Last        First       Salary
-------------------------------
Ling        mai         55900
Johnson     Jim         56500
Jones       Aaron       46000
Jones       Chris       34500
Swift       Geoffrey    14200
Xiong       Fong        65000
Zarneck     Sabrina     51500


제약 조건
* 데이터를 파싱하기 위해 CSV 파서를 사용하지 말고 자신만의 코드를 작성하여
  사용할 것.

* 컬럼의 줄을 맞추기 위해 공백 글자를 사용할 것
* 컬럼의 길이는 가장 긴 값에 해당하는 글자보다 한 글자 길게 정할 것

도전 과제
* Salary를 달러 표시와 자리수 구분 기호(,)를 사용하여 출력하도록 프로그램을
  수정해보자 v

* 결과를 Salary 값으로 내림차순으로 정렬하도록 프로그램을 수정해보자.
* CSV 파싱 라이브러리를 사용하도록 프로그램을 수정한 다음 그 결과를 비교하라.
'''

class InputError(BaseException):
    pass


class File(object):
    INT_NOT_SET = -1
    CHUNK_SIZE = 64 * 2 ** 10

    seek = property(lambda self: self.file.seek)
    read = property(lambda self: self.file.read)

    def __init__(self, file, name=None):
        self.file = file
        if name is None:
            self.name = getattr(file, 'name', None)
        self.name = name
        self.readlines = file.readlines()
        self.data = ''

    def chunks(self, chunk_size=None):
        chunk_size = chunk_size or self.CHUNK_SIZE

        self.seek(0)

        while True:
            data = self.read(chunk_size)
            if not data:
                break
            yield data

    def __iter__(self):
        '''newline은 \r, \r\n \n으로 올수가 있다.
        splitlines(True)는 \r,\n이 있으면 그것을 기준으로 리스트화한다.''' 

        buffer_ = None
        for chunk in self.chunks():
            for line in chunk.splitlines(True):
                ''' 버퍼가 있으면'''
                if buffer_:
                    '''\r 으로 끝나고, \n이 아닌 경우.'''
                    if endswith_cr(line) and not equals_lf(line):
                        yield line
                    else:
                        '''\r\n으로 끝날때, 또는 buffer에 newline이 없을 때 '''
                        line = buffer_ + line
                    ''' buffer는 line에 넣고 '''
                    buffer_ = None

                if endswith_lf(line):
                    '''line feed일 때, '''
                    yield line
                else:
                    ''' line feed, CR이 아닌 경우 buffer로 쌓인다.'''
                    buffer_ = line

        if buffer_:
            yield buffer_

    def show(self):
        for line in self:
            sys.stdout.write(line)


class CVSParse(object):
    def __init__(self, *args):
        self.col_names = args
        self.col_num = len(args)
        self.col_max = {}
        self.line = []

        for col in args:
            self.col_max[col] = 0

    def write(self):
        pass

    def parse(self, file):
        for line in file:
            data = []
            for i, col in enumerate(line.split(',')):
                if i > self.col_num:
                    raise InputError("Over columns...")
                
                cmax = len(col)
                name = self.col_names[i]
                self.col_max[name] = cmax if cmax > self.col_max[name] \
                        else self.col_max[name]
                data.append(col)
            self.line.append(data)

    def order(self, index=0, dec=True):
        def index_data(idx):
            return idx[index]

        if dec is True:
            self.line = sorted(self.line, key=index_data, reverse=True)
        else:
            self.line = sorted(self.line, key=self.line[index], reverse=False)

    def show(self, dollar=False):
        for i, col in enumerate(self.line):
            if i == 0:
                msg = ''
                for name in self.col_names:
                    cmax = self.col_max[name] + 1
                    msg += name.ljust(cmax) 
                print(msg)
                print('-' * len(msg))
            else:
                msg = ''
                for i, data in enumerate(col):
                    #data = data.strip()
                    name = self.col_names[i]
                    if name == 'Salary' and dollar is True:
                        data = '$' + data
                    cmax = self.col_max[name] + 1
                    msg += data.ljust(cmax) 
                print(msg)
        

def endswith_cr(line):
    """Return True if line (a text or byte string) ends with '\r'."""
    return line.endswith('\r' if isinstance(line, str) else b'\r')


def endswith_lf(line):
    """Return True if line (a text or byte string) ends with '\n'."""
    return line.endswith('\n' if isinstance(line, str) else b'\n')


def equals_lf(line):
    """Return True if line (a text or byte string) equals '\n'."""
    return line == ('\n' if isinstance(line, str) else b'\n')


if __name__ == "__main__":

    start = time.time()
    f = open("./ttt.csv", "r")
    new_file = File(f)
    c = CVSParse('Last', 'First', 'Salary')
    c.parse(new_file)
    c.order(2, dec=True)
    c.show(dollar=True)
    elapsed = time.time() - start
    print("the time is {}".format(elapsed))
    f.close()
    print("")

    start = time.time()
    with open("./ttt.csv", "rb") as f:
        spamleader = csv.reader(f, delimiter=',', quotechar='|')
        for row in spamleader:
            print ' '.join(row)
    elapsed = time.time() - start
    print("the time is {}".format(elapsed))

