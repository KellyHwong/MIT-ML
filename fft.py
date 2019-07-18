#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-11-19 19:34
# @Author  : Your Name (you@example.org)
# @Link    : https://zh.wikipedia.org/zh-cn/%E5%8D%B7%E7%A7%AF#%E8%A8%88%E7%AE%97%E7%A6%BB%E6%95%A3%E5%8D%B7%E7%A9%8D%E7%9A%84%E6%96%B9%E6%B3%95

import os
import numpy as np
import numpy.fft


def ft(f: list, g: list) -> list:
    """
    直接计算
    y_n = f_n * g_n = \sum_m=0^M-1{f_n-m}{g_m}
    复杂度
    O(MN)
    """
    N, M = len(f), len(g)
    if M > N:  # let M < N
        f, g = g, f
        M, N = N, M
    L = M + N - 1
    y = [0] * L
    for n in range(L):
        for m in range(M):
            if n-m not in range(N):
                continue
            print("m:{},n:{}".format(m, n))
            print(y)
            y[n] += f[n-m] * g[m]
    return y


def fft(f: list, g: list) -> list:
    return None


def main():
    f = [4, 5, 6, 7]
    g = [1, 2, 3]

    y = ft(f, g)
    # y = np.convolve(f, g)  # [ 4 13 28 34 32 21]
    print(y)


if __name__ == "__main__":
    main()
