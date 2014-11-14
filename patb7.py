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

max = input()
count = 0
lastPrime = 2

for i in range(2, max+1):
    if isPrime(i) == 0:
        if i - lastPrime == 2:
            count += 1
        
        lastPrime = i

print count                         
exit(0)
