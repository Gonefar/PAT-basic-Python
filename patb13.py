#!/usr/bin/python

from sys import exit
from math import sqrt

def isPrime( num ):
    if num == 1:
        return 1

    if num == 2 or num == 3:
        return 0

    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return 1

    return 0

str = raw_input().split()
start = int(str[0])
end = int(str[1])        
count = 0
i = 2
flag = 0
while True:
    if isPrime(i) == 0:
        count += 1
        if count >= start :
            flag += 1
            if flag % 10 != 0:
                print i,
            else:
                print i

        if count >= end:
            break
    i += 1
exit(0)
