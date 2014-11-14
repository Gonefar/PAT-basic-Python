#!/usr/bin/python

from sys import exit
str = raw_input().split()
num = [int(str[i]) for i in range(len(str))]        
out = ''

flag = 0
for i in range(1, len(num)+1):
    if num[i] != 0:
        flag = i
        break
out += '%d' % flag
for i in range(len(num)):
    if i == flag:
        out += ('%s' % i) * (num[i]-1)
    else:
        out += ('%s' % i) * num[i]

print out        
exit(0)
