#!/usr/bin/python

from sys import exit
str = raw_input()
sum = 0

for i in str:
    sum += int(i)

sumStr = '%d' % sum
str = ""
for i in range(len(sumStr)):
    if i == len(sumStr)-1:
        flag = ''
    else:
        flag = ' '

    if sumStr[i] == '1':
        str += 'yi' + flag
    if sumStr[i] == '2':
        str += 'er' + flag
    if sumStr[i] == '3':
        str += 'san' + flag
    if sumStr[i] == '4':
        str += 'si' + flag
    if sumStr[i] == '5':
        str += 'wu' + flag
    if sumStr[i] == '6':
        str += 'liu' + flag
    if sumStr[i] == '7':
        str += 'qi' + flag
    if sumStr[i] == '8':
        str += 'ba' + flag
    if sumStr[i] == '9':
        str += 'jiu' + flag
    if sumStr[i] == '0':
        str += 'ling' + flag

print str       
exit(0)
