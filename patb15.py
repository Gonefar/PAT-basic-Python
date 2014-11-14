#!/usr/bin/python

from sys import exit

def myCmp( a, b ):
    valuea = 2 * int(a[1]) + int(a[2])
    valueb = 2 * int(b[1]) + int(b[2])
    
    if valuea > valueb:
        return -1
    elif valuea == valueb:
        if a[0] < b[0]:
            return -1
        else:
            return 1
    else:
        return 1

rawIn = raw_input().split()
num = int(rawIn[0])
jige = int(rawIn[1])
prio = int(rawIn[2])

firstClass = []
secondClass = []
thirdClass = []
forthClass = []

for i in range(num):
    rawIn = raw_input().split()
    
    if int(rawIn[1]) >= prio and int(rawIn[2]) >= prio:
        firstClass.append(rawIn)
    elif int(rawIn[1]) >= prio and jige <= int(rawIn[2]) <= prio:
        secondClass.append(rawIn)
    elif int(rawIn[1]) >= jige and int(rawIn[2]) >= jige and int(rawIn[1]) >= int(rawIn[2]):        
        thirdClass.append(rawIn)
    elif int(rawIn[1]) >= jige and int(rawIn[2]) >= jige:
        forthClass.append(rawIn)
    else:
        pass

firstClass.sort(cmp=myCmp)
secondClass.sort(cmp=myCmp)
thirdClass.sort(cmp=myCmp)
forthClass.sort(cmp=myCmp)        

print len(firstClass) + len(secondClass) + len(thirdClass) + len(forthClass)
for i in [firstClass, secondClass, thirdClass, forthClass]:
    for j in i:
        print j[0], j[1], j[2]

exit(0)
