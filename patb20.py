#!/usr/bin/python

from sys import exit

str = raw_input().split()
mkNum = int(str[0])        
total = int(str[1])
para = []
para.append(raw_input().split())
para.append(raw_input().split())        

for i in range(mkNum):
    para[0][i] = float(para[0][i])
    para[1][i] = float(para[1][i])

dict = {}
for i in range(mkNum):
    if (float(para[1][i]) / para[0][i]) in dict.keys():
        dict[float(para[1][i]) / para[0][i]][0] += para[1][i]
        dict[float(para[1][i]) / para[0][i]][1] += para[0][i]
    else:
        dict[float(para[1][i]) / para[0][i]] = [para[1][i], para[0][i]]

mkeys = dict.keys()
mkeys.sort()
mkeys.reverse()            
value = 0.0

for i in mkeys:
    if total > dict[i][1]:
        value += dict[i][0]
        total -= dict[i][1]
    else:
        value += float(dict[i][0]) / dict[i][1] * total
        break

print '%.2f' % value

exit(0)
