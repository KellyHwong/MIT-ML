import numpy as np
import random


N = 10


def null(a, rtol=1e-5):
    u, s, v = np.linalg.svd(a)
    rank = (s > rtol*s[0]).sum()
    return rank, v[rank:].T.copy()


def gen_data(N, noisy=False):
    lower = -1
    upper = 1
    dim = 2

    X = np.random.rand(dim, N)*(upper-lower)+lower

    while True:
        Xsample = np.concatenate(
            (np.ones((1, dim)), np.random.rand(dim, dim)*(upper-lower)+lower))
        k, w = null(Xsample.T)
        y = np.sign(np.dot(w.T, np.concatenate((np.ones((1, N)), X))))
        if np.all(y):
            break

    return (X, y, w)


def change_label(y):
    idx = random.sample(range(1, N), N/10)
    y[idx] = -y[idx]
    return y


if __name__ == '__main__':
    X, y, w = gen_data(10)
    print(X)
