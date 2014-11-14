#!/usr/bin/python

from sys import exit
num = input()

for i in range(num):
    str = raw_input().split()
    numList = [int(str[j]) for j in range(len(str))]
    if numList[0] + numList[1] > numList[2]:
        print 'Case #%d: true' % (i+1)
    else:
        print 'Case #%d: false' % (i+1)

exit(0)
