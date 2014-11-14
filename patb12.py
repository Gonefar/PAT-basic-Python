#!/usr/bin/python

from sys import exit

str = raw_input().split()
numList = [int(str[j]) for j in range(len(str))]
numList = numList[1:]
sum = 0
for i in numList:
    if i % 5 == 0 and i % 2 == 0:
        sum += i

if sum == 0:
    print 'N',
else:
    print sum,

sum = 0
count = 0
flag = 1
for i in numList:
    if i % 5 == 1:
        sum += i * flag
        flag *= -1
        count += 1

if count == 0:
    print 'N',
else:
    print sum,

sum = 0
for i in numList:
    if i % 5 == 2:
        sum += 1

if sum == 0:
    print 'N',
else:
    print sum,

sum = 0.0
count = 0
for i in numList:
    if i % 5 == 3:
        count += 1;
        sum += float(i)

if count == 0:
    print 'N',
else:
    print '%.1f' % (sum / float(count)),

max = 0
for i in numList:
    if i % 5 == 4:
        if i > max:
            max = i

if max == 0:
    print 'N'
else:
    print max

exit(0)
