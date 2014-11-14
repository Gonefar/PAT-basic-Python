#!/usr/bin/python
from sys import exit
x = int( raw_input() )
path = 0

while 1:
	if x == 1:
		break

	if x % 2 == 0:
		x /= 2
	else:
		x = ( 3 * x + 1 ) / 2
	
	path += 1
	
	if x == 1:
		break

print path
exit(0)
