#!/usr/bin/python

from sys import exit

def addFact( factList, keyList, key ):
    if key in factList or key in keyList:
        return 1
    keyList.append(key)
    factList.append(key)

    while True:
        if key == 1:
            if not key in factList:
                factList.append(key)
            break               
        if key % 2 == 0:
            key /= 2
        else:
            key = ( 3 * key + 1 ) / 2

        if (not key in keyList):
            if (not key in factList):
                factList.append(key)
        else:
            keyList.remove(key)

num  = input()
numList = raw_input().split()
numList = [int(numList[i]) for i in range(len(numList))]        
factList = []
keyList = []

for i in numList:
    addFact(factList, keyList, i)

keyList.sort()
keyList.reverse()

for i in range(len(keyList)):
    if i != len(keyList)-1:
        print keyList[i],
    else:
        print keyList[i]

exit(0)
