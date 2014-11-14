#!/usr/bin/python

from sys import exit
str = raw_input().split()
numList = [int(str[i]) for i in range(len(str))]        

for i in range(len(numList)/2):
    if numList[2 * i + 1] == 0:
        numList[2 * i] = 0
    else:
        numList[2 * i] *= numList[2 * i + 1]
        numList[2 * i + 1] -= 1

out = ''        
for i in range(len(numList)/2):
    if numList[2 * i] == 0 and numList[2 * i + 1] == 0:
        continue

    if i == 0 and (numList[1] != 0 or numList[0] != 0):
        out += '%d %d' % (numList[0], numList[1])
    else:
        out += ' %d %d' % (numList[2*i], numList[2*i+1])

if len(out) == 0:
    print '0 0'
else:
    print out        
exit(0)
