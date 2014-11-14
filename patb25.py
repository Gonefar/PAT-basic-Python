#!/usr/bin/python

from sys import exit
str = raw_input().split()
dict = {}
ListLen = int(str[1])        
revsLen = int(str[2])
list = []

for i in range(ListLen):
    tmp = raw_input().split()
    dict[tmp[0]] = tmp[1:]        

cur = str[0]                                  
for i in range(ListLen):
    list.append([cur, dict[cur][0], dict[cur][1]])
    cur = dict[cur][1]                                                  

count = 0
revList = []
while ListLen - count >= revsLen:
    y=list[count:count+revsLen]
    y.reverse()
    count += revsLen
    revList.extend(y)

revList.extend(list[count:])        
cur = revList[0][0]
count = 0

while ListLen - count >= revsLen:
    for i in range(revsLen-1):
        revList[count+i][2] = revList[count+i+1][0]
    
    if count + revsLen < ListLen:
        revList[count+revsLen-1][2] = revList[count+revsLen][0]

    count += revsLen

revList[-1][2] = '-1'
for i in range(ListLen):
    print revList[i][0], revList[i][1], revList[i][2]
                          
exit(0)
