#!/usr/bin/python

from sys import exit
str1 = raw_input()
str2 = raw_input()
str3 = ""

for ch in str1:
    if not ch in str2:
        if not (ch in str3 or ch.upper() in str3):
            str3 += ch.upper()

print str3

exit(0)
