#!/usr/bin/python

from sys import exit

dict_week = {'A':'MON', 'B':'TUE', 'C':'WED', 'D':'THU', \
            'E':'FRI', 'F':'SAT', 'G':'SUN'}
dict_hour = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5,'6':6, \
             '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, \
             'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':18, \
             'J':19, 'K':20, 'L':21, 'M':22, 'N':23}

str = []
for i in range(4):
    str.append(raw_input())

res = []
count = 0

for i in range(len(str[0])):
    if count == 0 and str[0][i] == str[1][i] and str[0][i] in dict_week.keys():
        res.append(str[0][i])
        count += 1
        continue                  
    
    if count == 1 and str[0][i] == str[1][i] and str[0][i] in dict_hour.keys():
        res.append(str[0][i])
        break

for i in range(len(str[2])):
    if str[2][i] == str[3][i] and str[2][i].isalpha():
        res.append(i)
        break

print '%s %02d:%02d' % (dict_week[res[0]], dict_hour[res[1]], res[2])
    
exit(0)
