#!/usr/bin/python

from sys import exit
str = raw_input().split()
sum = 0
if str[0].count(str[1]) != 0:
    sum += int(str[0].count(str[1]) * str[1])

if str[2].count(str[3]) != 0:
    sum += int(str[2].count(str[3]) * str[3])

print sum        
exit(0)
