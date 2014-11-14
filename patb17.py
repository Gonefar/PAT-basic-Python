#!/usr/bin/python

from sys import exit
str = raw_input().split()
a = str[0]
b = int(str[1])
add = 0
shang = ''

for i in a:
    shang += '%d' % ( (int(i)+add*10) / b )
    add = (int(i)+add*10) % b

shang = shang.lstrip('0')
if shang == '':
    shang = '0' 
print shang, add        
exit(0)
