#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-01-19 10:24
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org

import os
import numpy as np

a = [[1, 2, 3],
     [4, 5, 6],
     [1, 2, 1]]
a = np.asarray(a)

print(a.T)

print(np.linalg.det(a))
print(np.linalg.det(a.T))

g = np.asarray([2, 1, 3])
print(np.dot(g, a))
print(np.dot(a, g))

b = [[2, 1, 0],
     [1, 4, 4],
     [5, 6, 4]]
b = np.asarray(b)
rank = np.linalg.matrix_rank(b)
print(rank)

inv = np.linalg.inv(a)
print(inv)  # inverse of a
print(np.dot(a, inv))
