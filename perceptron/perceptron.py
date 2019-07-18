#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-17-19 19:40
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org

import os
import numpy as np


def main():
    '''
    dataArr = [-0.2, -1.1, 0, 2.3, 4.5, 0.0]
    print(dataArr)
    signResult = np.sign(dataArr)
    print(signResult)
    '''

    # 输入数据
    X = np.array([[1, 1, 2, 3],
                  [1, 1, 4, 5],
                  [1, 1, 1, 1],
                  [1, 1, 5, 3],
                  [1, 1, 0, 1]])
    # 权重初始化，取值范围-1到1
    print(X.shape[1])
    W = (np.random.random(X.shape[1])*2)-1
    print('初始化权值：', W)


if __name__ == "__main__":
    main()
