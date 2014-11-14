#!/usr/bin/python

from sys import exit
str = raw_input().split()

num = int(str[0]) + int(str[1])
d = int(str[2])

list = []
out = ''

if num == 0:
    out = '0'
while num != 0:
    list.append(num % d)
    num /= d

list.reverse()
for i in list:
    out += '%d' % i

print out    
exit(0)
