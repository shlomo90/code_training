# -*- encoding: utf-8 -*-

import os, sys, tty, termios
import fcntl
import time
import signal
from pastie_client import client_pastie

CMD_CONTINUE = 0
CMD_EXIT = 1 << 0

NEWLINE = '\r'
QUESTION = '?'
ALPHA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGIT = "0123456789"
SPECIAL = "!\"#$%&\'()*+,-./:;<=>@[\\]^_`{|}~"
SPACE = ' '
DELETE = chr(127)   # delete key is ASCII 127
TAB = chr(9)

def timeout_shell(signum, frame):
    sys.exit(1)


def do_shell(prompt, timeout=60):
    fd = sys.stdin.fileno()
    signal.signal(signal.SIGALRM, timeout_shell)
    sys.stdout.write(prompt + ' >')

    line_buf = []
    while (True):
        signal.alarm(timeout)
        ch = get_ch(fd) # Blocking
        signal.alarm(0)

        if (ch == QUESTION or ch == TAB):
            help_cmd()
            sys.stdout.write('\r' + prompt + ' >' + ''.join(line_buf))
            continue
        elif (ch in ALPHA or ch in DIGIT or ch in SPECIAL or ch in SPACE):
            line_buf.append(ch)
            sys.stdout.write(ch)
            continue
        elif (ch == DELETE):
            if len(line_buf) > 0:
                del(line_buf[-1])
            sys.stdout.write('\x1b[2K')  # delete current line
            sys.stdout.write('\r' + prompt + ' >' + ''.join(line_buf))
            continue 
        elif (ch == NEWLINE):
            cmd = ''.join(line_buf)
            sys.stdout.write('\n')
            status, prompt = command_handler(cmd, prompt)
            if (status & CMD_EXIT):
                break
            line_buf = []
            sys.stdout.write(prompt + ' >')
        else:
            print "\n invalid character {} \n".format(ch)


def command_handler(cmd, prompt):
    default = "pastie"
    get_menu = "pastie-get"
    put_menu = "pastie-put"
    prompt = prompt
    if prompt == default:
        if cmd == 'exit':
            return CMD_EXIT, prompt
        elif cmd == 'clear':
            os.system("clear")
        elif cmd == 'get':
            prompt = get_menu
        elif cmd == 'put':
            prompt = put_menu
        else:
            if len(cmd) > 0:
                print "Invalid Command: {}".format(cmd)
    elif prompt == get_menu:
        ret = client_pastie().get_message(cmd)
        prompt = default
        print "msg = {}".format(ret)
    elif prompt == put_menu:
        ret = client_pastie().put_message(cmd)
        status = ret.split()[0]
        if status == 'ok':
            hash_value = ret.split()[1]
            print 'message is saved in "{}"'.format(hash_value)
        else:
            print 'putting message failed'
        prompt = default
    return CMD_CONTINUE, prompt


def get_ch(fd):
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch


def help_cmd():
    def _wrap(text):
        print "\n{}".format(text)

    _wrap("############## HELP ###############")
    _wrap("Commands : ")
    _wrap("    new        : Make a new text")
    _wrap("    get <URI>  : Get the text from the uri")
    _wrap("    edit <URI> : Edit the text from the uri")
    _wrap("    exit       : Exit the program")
    _wrap("    clear      : Clear the screen")
