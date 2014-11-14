#!/usr/bin/python

from sys import exit

str = raw_input()
str = (4-len(str))*'0' + str
strList = sorted(str)

while strList.count(str[0]) != 4:
    strList = sorted(str)
    small = ''
    big = ''
    res = ''
    for i in range(4):
        small += strList[i]

    strList.reverse()
    for i in range(4):
        big += strList[i]

    str = '%04d' % (int(big)-int(small))
    print '%s - %s = %s' % (big, small, str)
    
    if str == '6174':
        break

if strList.count(str[0]) == 4:
    print '%s - %s = 0000' % (str, str)

exit(0)
