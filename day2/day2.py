import sys
import numpy as np
import os

file = open('day2input.tsv', 'r')
input = file.read()

df = np.asarray(input.split('\n'))
df = np.array([x.split('\t') for x in df])
vfunc = np.vectorize(int)
df=vfunc(df)

diffs = 0
for i in range(df.shape[0]):
    diffs = diffs + (max(df[i])-min(df[i]))
print diffs

divs = 0
for i in range(df.shape[0]):
    for k in range(df.shape[1]):
        for j in range(k+1,df.shape[1]):
            if df[i][k]%df[i][j] == 0:
                divs = divs + df[i][k]/df[i][j]
            elif df[i][j]%df[i][k] == 0:
                divs = divs + df[i][j]/df[i][k]

print divs
