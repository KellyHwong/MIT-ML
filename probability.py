#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-01-19 12:50
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org

import os
from scipy.integrate import quad
from numpy import sqrt, pi, exp


def gaussian(x, mu, sigma):
    return 1/sqrt(2*pi*sigma**2)*exp(-((x-mu)/sigma)**2/2)


if __name__ == "__main__":
    mu, sigma = 1, sqrt(2)
    a, b = 0.5, 2
    I = quad(gaussian, a, b, args=(mu, sigma))
    print(I)
