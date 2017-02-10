#! /usr/bin/python3

import sys

def Main():
    filename = sys.argv[1]
    f = open(filename, 'r')
    
    names = f.readlines()
    for name in names:
        name = name.replace('\n', '')
        if name.strip() != "":
            print(name)

if __name__ == '__main__':
    Main()
