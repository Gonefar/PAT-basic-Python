#!/usr/bin/python

from sys import exit
str = raw_input().split('E')

if str[1] != '':
    index = int(str[1])
else: 
    index = 0

num = str[0]
intPart = num.split('.')[0]
xsPart = num.split('.')[1]
out = ''

if num[0] == '-':
    out += '-'

if index == 0:
    out = str[0]
elif index > 0:
    out += '%d' % int(abs(int(intPart)))
    if len(xsPart) <= index:
        out += xsPart
        out += '0' * (index - len(xsPart))
    else:
        out += xsPart[:index]
        out += '.'
        out += xsPart[index:]
else:
    out += '0.'
    out += '0' * (abs(index)-1)
    out += '%d' % int(abs(int(intPart)))
    out += xsPart

print out    
exit(0)
