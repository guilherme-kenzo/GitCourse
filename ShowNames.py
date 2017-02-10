#! /usr/bin/python3

import sys

filename = sys.argv[1]
f = open(filename, 'r')

names = f.readlines()
for name in names:
    name = name.replace('\n', '')
    if name.strip() != "":
        print(name)
