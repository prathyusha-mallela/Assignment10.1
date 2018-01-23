# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 21:23:32 2018

@author: Prathyusha Mallela
"""

import numpy as np
def moving_average(x, N):
    cumsum = np.cumsum(np.insert(x, 0, 0)) 
    return (cumsum[N:] - cumsum[:-N]) / float(N)

means=moving_average([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150],3)
print(means)