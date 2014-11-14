#!/usr/bin/python

from sys import exit
str = raw_input()
strLen = len(str)
out = ''

for i in range(strLen):
    if strLen - i == 3:
        out += 'B' * int(str[i])
    elif strLen - i == 2:
        out += 'S' * int(str[i])
    else:
        for i in range(1, int(str[i]) + 1):
            out += '%s' % i

print out            
exit(0)
