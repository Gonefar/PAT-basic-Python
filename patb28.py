#!/usr/bin/python

from sys import exit

def isValid( birth ):
    if birth <= "2014/09/06" and birth >= "1814/09/06":
        return 0
    else:
         return 1

str = raw_input()
num = int(str)
max = []
min = []
validNum = 0

for i in range(num):
    tmp = raw_input().split()
    if isValid( tmp[1] ) == 0:
        validNum += 1                              
        if len(max) == 0 or max[1] > tmp[1]:
            max = tmp

        if len(min) == 0 or min[1] < tmp[1]:
            min = tmp
if len(max) != 0:
    print validNum, max[0], min[0]
else:
    print '0'

exit(0)
