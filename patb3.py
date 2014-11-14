#!/usr/bin/python

from sys import exit

def isValid( strList ):
    if strList.count('P') != 1 or strList.count('T') != 1:
        return 1
    
    pIndex = strList.index('P')
    tIndex = strList.index('T')

    if pIndex == 0 and tIndex == 1:
        return 1
    
    listLen = len(strList)        
    if (pIndex * (tIndex - pIndex-1) != listLen - 1 - tIndex):                
        return 1

    keyNum = 0        
    for i in strList:
        if i == 'A' or i == 'P' or i == 'T':
            keyNum += 1

    if len(strList) != keyNum:
        return 1
    else:
        return 0

num = int(raw_input())
list = []

for i in range(num):
    str = raw_input()
    for j in str:
        list.append(j)
    if isValid(list) == 0:
        print 'YES'
    else:
        print 'NO'
    list = []                        

exit(0)
