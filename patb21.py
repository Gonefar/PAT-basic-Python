#!/usr/bin/python

from sys import exit
str = raw_input()

digit = []
for i in str:
    digit.append(i)

for i in range(10):
    if digit.count('%d' % i) > 0:
        print '%d:%d' % (i, digit.count('%d' % i))

exit(0)
