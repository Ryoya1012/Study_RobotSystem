#!/usr/bin/python3

import sys
sum = 0

def tonum(s):
    try:
        return  int(s)

    except:
        return  float(s)

for line in sys.stdin:
    sum += tonum(line)

print(sum)
