#!/usr/bin/python

from sys import exit
str = raw_input()

for i in range(len(str)):
	if str[i] == ' ':
		flag = i
		break

c1 = int(str[:flag])
c2 = str[flag+1:]

c1 += 1
num = 0
i = 0
while 1:
	c1 -= 2 * ( 2 * i + 1 )
	i += 1
	num += 1

	if c1 < 2 *(2 * i + 1):
		break

for j in range(num):
	print "%s%s" % (j*' ', ( 2*(num-1-j) + 1 )*c2)

for j in range(1,num):
	print "%s%s" % ( (num-j-1)*' ', (2*j + 1)*c2)

print c1
exit(0)
