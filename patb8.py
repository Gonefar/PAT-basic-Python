#!/usr/bin/python

from sys import exit
str = raw_input()
num = int(str.split()[0])
shift = int(str.split()[1])
shift %= num
numList = raw_input().split()    
numList = [int(numList[i]) for i in range(len(numList))]

out = ''
for i in range(len(numList)):
    if i != len(numList) - 1:
        print numList[(num-shift+i)%num],
    else:
        print numList[(num-shift+i)%num]
exit(0)
