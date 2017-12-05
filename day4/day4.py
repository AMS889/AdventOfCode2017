import sys
import numpy as np
import os

file = open('day4input.txt', 'r')
input = file.read()
input = input.split('\n')

masterlist = []
for i in range(len(input)):
    masterlist.append([input[i]])

split_master = []
for j in range(len(masterlist)):
    for i in masterlist[j]:
        split_master.append(i.split(' '))

total=0
for i in range(len(split_master)):
    if len(list(set(split_master[i])))==len(split_master[i]):
        total=total+1
print total

split_master_pt2 = []
for j in range(len(masterlist)):
    for i in masterlist[j]:
        test=[]
        for item in i.split(' '):
            test.append(''.join(sorted(item)))
        split_master_pt2.append(test)

total=0
for i in range(len(split_master_pt2)):
    if len(list(set(split_master_pt2[i])))==len(split_master_pt2[i]):
        total=total+1
print total
