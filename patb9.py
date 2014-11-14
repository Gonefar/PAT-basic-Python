#!/usr/bin/python

from sys import exit
str = raw_input()

   
tstr = str.strip();
tstr = tstr.split()
tstr.reverse()
revStr = tstr[0]

for i in range( len(tstr) ):
    if i != 0:
        revStr += ' '
        revStr += tstr[i]
print revStr                                
exit(0)                       
