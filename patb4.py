#!/usr/bin/python

from sys import exit
num = input()
max = []
min = []

for i in range(num):
    stud = raw_input().split()
    if len(max) == 0 or int(stud[2]) > int(max[2]):
        max = stud

    if len(min) == 0 or int(stud[2]) < int(min[2]):
        min = stud

print max[0], max[1]
print min[0], min[1]
exit(0)
