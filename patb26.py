#!/usr/bin/python

from sys import exit
str = raw_input()

for i in range(len(str)):
	if str[i] == ' ':
		flag = i
		break

c1 = int(str[:flag])
c2 = int(str[flag+1:])

CTK = 100

sec_sum = (c2 - c1) / CTK

if (c2 - c1) % 100 >= 50:
	sec_sum += 1

hh = sec_sum / 3600
mm = (sec_sum % 3600) / 60
ss = sec_sum % 60

print "%02d:%02d:%02d" % (hh, mm, ss)
exit(0)
