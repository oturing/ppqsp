#!/usr/bin/env python

import sys

def interactive_reader():
    while True:
        try:
            line = raw_input('> ')
        except KeyboardInterrupt:
            print
            break
        if line.strip() == 'quit':
            break
        yield line

def file_reader(file_name):
    with open(file_name) as f:
        for line in f:
            yield line.rstrip()

def repl(line_reader, echo):
    for line in line_reader:
        if echo:
            print ':', line
        line = line.strip()
        if line.startswith('print '):
            print line[6:]
        
if __name__=='__main__':
    if len(sys.argv) == 1:
        line_reader = interactive_reader()
        echo = True
    else:
        line_reader = file_reader(sys.argv[1])
        echo = False
    repl(line_reader, echo)

