import sys
import numpy as np
import os

file = open('day5input.txt', 'r')
input = file.read()
input2 = input.split('\n')
input = input.split('\n')

input2 = [ int(x) for x in input2 ]
input = [ int(x) for x in input ]

i=0
counter=0
while i < len(input):
    steps = input[i]
    input[i] = input[i]+1
    i=i+steps
    counter=counter+1
print counter

i=0
counter=0
while i < len(input2):
    steps = input2[i]
    if input2[i] >= 3:
        input2[i] = input2[i] -1
    elif input2[i] < 3:
        input2[i] = input2[i]+1
    i=i+steps
    counter=counter+1
print counter
