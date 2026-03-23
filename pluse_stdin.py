#!/usr/bin/python3

import sys
sum = 0.0

for line in sys.stdin:
    
    num = float(line)
    
    sum += num

print(sum)
