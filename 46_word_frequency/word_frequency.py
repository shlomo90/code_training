# -*- encoding: utf-8 -*-

'''
파일을 읽은 다음 파일에서 사용된 단어의 빈도를 세는 프로그램을 작성하라.
단어의 빈도를 측정한 후에는 단어와 빈도를 히스토그램 형태로 화면에 나타내보자

출력 예
제공된 파일에 들어있는 내용:

badger  badger  badger badger  mushroom  mushroom
snake badger  badger badger

프로그램이 만든 출력 결과:

badger : *******
mushroom : **
snake : *

제약 조건

* 가장 많이 사용된 단어를 맨 위에, 가장 적게 사용된 단어를 마지막에 나타나도록
  구현할 것.


도전 과제
* 그래픽 프로그램으로 작성한 다음, 결과를 바 그래프로 나타내도록 하라.
* 셰익스피어의 멕베스와 같이 굉장히 큰 파일을 입력으로 사용하여 프로그램 성능을
  측정하라. 그런 다음 프로그램이 최대의 성능을 낼 수 있도록 알고리즘을 개선하라
* 다른 프로그래밍 언어로 동일한 프로그램을 작성한 후 두 언어로 작성한 프로그램
  의 성능을 비교하라.
'''


FILE_PATH = "./test.txt"
#FILE_PATH = "./macbeth.txt"


class WordStat(object):
    CHUNK_SIZE = 4096

    def __init__(self, f):
        self.words = {}

        if isinstance(f, file):
            self.file = f
        else:
            print("The Parameter is not file object!")

        # Do read words.
        word = []   #A list of characters of word.
        on_alpha = False
        for buf in self._chunk(self.CHUNK_SIZE):
            for c in buf:
                if c.isalpha():
                    on_alpha = True
                    word.append(c)
                elif on_alpha is True:
                    on_alpha = False
                    if word:
                        word_str = ''.join(word)
                        if word_str in self.words:
                            self.words[word_str] += 1
                        else:
                            self.words[word_str] = 1
                        word = []


        if word:
            word_str = ''.join(word)
            if word_str in self.words:
                self.words[word_str] += 1
            else:
                self.words[word_str] = 1
            word = []

        self.close()

    def _chunk(self, size):
        chunk_size = size
        self.file.seek(0)

        while(True):
            ''' read()
            Args:
                the size of the file
            return:
                byte size which is read or "" if no read data.

            read 함수는 읽은 data리턴, 또는 더이상 읽을것이 없으면 "" 리턴'''
            data = self.file.read(chunk_size)
            if not data:
                break
            else:
                yield data

    def make_tuplelist(self):
        inc_order = []
        for key, value in self.words.iteritems():
            tup = (key, value)
            inc_order.append(tup)

        return inc_order

    def order_freq_list(self, l):
        ret = sorted(l, key=lambda word: word[1], reverse=True)
        return ret

    def show_list(self):
        t_list = self.make_tuplelist()
        t_list = self.order_freq_list(t_list)

        for tup in t_list:
            word = tup[0]
            freq = tup[1]

            print("{}: {}".format(word, "*" * freq))

    def close(self):
        self.file.close()

if __name__ == "__main__":
    f = open(FILE_PATH, "r") 
    w = WordStat(f)
    w.show_list()
