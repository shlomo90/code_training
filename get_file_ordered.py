# -*- encoding: utf-8 -*-

import os
import re


if __name__ == "__main__":
    for d in os.listdir("."):
        m = re.search("(.*)_([0-9]+)", d)
        if m:
            name = m.group(1)
            number = int(m.group(2))
            number = "{0:0{1}d}".format(number, 2)
            new = number + "_" + name
            os.system("mv ./{} {}".format(d, new))
