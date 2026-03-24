#!/usr/bin/python3

import sys
sum = 0

for line in sys.stdin:
    
    try:
        sum += int(line)
    #num = float(line)

    except:
        sum += float(line)

print(sum)
