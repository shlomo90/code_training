# -*- encoding:utf-8 -*-

'''
First, These Modules are doing text searching or replacing or getting the
number of the sentences or words.

The List of Directives

1. word_manip

'''

import os
import shutil

TEMP_DIR = "/tmp"


class WordManip(object):
    BUFFER_SIZE = 2048

    def __init__(self, match, replace):
        self.match = match
        self.replace = replace

    def execute(self, loc):
        path = loc.path
        cur = loc.cur_loc

        list_files = os.listdir(path)
        txt_files = []
        for f in list_files:
            if f.endswith(".txt"):
                txt_files.append(f)

        for t in txt_files:
            temp_file = TEMP_DIR + "/" + t
            dest_file = path + t

            t = open(temp_file, "w")
            f = open(dest_file, "r")
            match = self.match
            replace = self.replace
            is_matching = False
            match_len = len(match)
            replace_buf = []
            match_word = []
            idx = 0
            try:
                for buf in self._chunks(f):
                    for b in list(bytearray(buf)):
                        if ord(match[idx]) == b:
                            idx += 1
                            is_matching = True
                            match_word.append(b)
                        else:  # not match
                            if match_word:
                                replace_buf += match_word
                                replace_buf.append(b)
                            else:
                                replace_buf.append(b)
                            is_matching = False
                            idx = 0
                            match_word = []

                        if idx == match_len:
                            replace_buf = replace_buf \
                                + list(bytearray(self.replace))
                            is_matching = False
                            idx = 0
                            match_word = []

                    #write temp file
                    replace_buf = [chr(b) for b in replace_buf]
                    t.write(''.join(replace_buf).decode("utf-8"))
                    replace_buf = []
            except BaseException as e:
                f.close()
                t.close()
                os.remove(temp_file)
                print(e)
                raise

            f.close()
            t.close()
            shutil.move(temp_file, dest_file)

    def _chunks(self, f):
        chunk_size = self.BUFFER_SIZE

        f.seek(0)

        while True:
            data = f.read(chunk_size)
            if not data:
                break
            yield data
