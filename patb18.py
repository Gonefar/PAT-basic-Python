#!/usr/bin/python

from sys import exit

def output_popular( dict ):
    popular = ''
    num = 0
    for i in dict.keys():
        if popular == '' or dict[i] > num or (dict[i] == num and i < popular):
            popular = i
            num = dict[i]

    return popular

dict_pri_jia = {'B C':0, 'B B':1, 'B J':2, 'C B':2, 'C C':1, 'C J':0, 'J B':0, 'J J':1, 'J C':2}        
jia = [0, 0, 0, {'B':0, 'C':0, 'J':0}]
yi = [0, 0, 0, {'B':0, 'C':0, 'J':0}]

num = input()
for i in range(num):
    str = raw_input()
    
    jia[dict_pri_jia[str]] += 1
    yi[2-dict_pri_jia[str]] += 1
    
    if dict_pri_jia[str] == 0:
        jia[3][str[0]] += 1

    if dict_pri_jia[str] == 2:
        yi[3][str[2]] += 1

print jia[0], jia[1], jia[2]
print yi[0], yi[1], yi[2]
print output_popular(jia[3]), output_popular(yi[3])

exit(0)
