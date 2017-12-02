import sys
import os

file = open('day1input.txt', 'r')

numberlist = file.read()

#Part1

total=0
for i in range(len(numberlist)):
    if i == 0:
        first_digit=int(numberlist[i])
    elif (i>0 and i<len(numberlist)-1):
        if int(numberlist[i])==int(numberlist[i+1]):
            total=total+int(numberlist[i])
    elif i==len(numberlist)-1:
        if int(numberlist[i])==first_digit:
            total=total+int(numberlist[i])
print total

#Part2
total=0
for i in range(len(numberlist)):
    if int(numberlist[i])==int(numberlist[(i+(len(numberlist)/2))%len(numberlist)]):
        total=total+int(numberlist[i])
print total
