import sys
import numpy as np
import os

import math

def side_len(number):
    side = math.ceil(math.sqrt(number))
    if side % 2 != 0:
        side = side
    else:
        side = side + 1
    dist_cent = (side-1)/2
    for i in range(4):
        axises = [side**2 - ((side-1) * i)  - math.floor(side/2)] #get the axis "cells"
    dist_perp = min([abs(axis - input) for axis in axises])
    print(dist_perp + dist_cent)

side_len(361527)
