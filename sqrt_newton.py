#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-01 20:13:43
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

def sqrt_newton(y):
    if y < 0:
        return None
    err = 1e-7
    xn = y
    while abs(y - xn*xn) > err:
        xn = (y/xn + xn) / 2.0;
        print(xn)
    return xn

def main():
    print(sqrt_newton(2))

if __name__ == '__main__':
    main()