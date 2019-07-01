#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jun-30-19 20:16
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org

import os
import numpy as np


def funcname(parameter_list):
    pass


def main():
    theta = np.asarray([3, 1])
    theta0 = -1
    a = np.asarray([-1, -1])
    r1 = (np.dot(a, theta) + theta0) / np.linalg.norm(theta)
    print(r1)

    o = np.asarray([0, 0])
    r2 = (np.dot(o, theta) + theta0) / np.linalg.norm(theta)
    print(r2)

    # 3 x1 + 1 x2 + -1 = 0
    # (1, -2), (2, -5)
    # (1, -3) 即直线的方向向量
    d = np.asarray([1, -3])
    p1 = np.dot(a, theta) / np.linalg.norm(theta)
    print(p1)

    p2 = np.dot(a, d) / np.linalg.norm(d)
    print(p2)


if __name__ == "__main__":
    main()
