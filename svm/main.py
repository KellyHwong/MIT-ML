#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Aug-09-19 14:06
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org

import os
import utils


def test_sklearn():
    from sklearn import svm

    X = [[0, 0], [2, 2]]
    y = [0.5, 2.5]
    clf = svm.SVR(C=1.0, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma="auto",
                  kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)
    clf.fit(X, y)

    print(clf.predict([[1, 1]]))


def test_toy_data():
    toy_features, toy_labels = toy_data = utils.load_toy_data('toy_data.tsv')

    from sklearn import svm
    clf = svm.SVR(C=1.0, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma="auto",
                  kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)
    clf.fit(toy_features, toy_labels)
    # print(clf.coef_) # coef_ is only available when using a linear kernel
    print(clf.dual_coef_)


def main():
    # test_sklearn()
    test_toy_data()


if __name__ == "__main__":
    main()
