import numpy as np


def getNAs(N): # returns N sample A matrices
    NAs = []
    for h in range(N):
        A = np.random.binomial(size = (15, 15), n = 1, p = 0.1)
        for i in range(15):
            for j in range(15):
                if i < 5 :
                    if j < 5:
                        A[i][j] = np.random.binomial(size = 1, n = 1, p = 0.6)
                elif i < 10:
                    if j < 10 and j >= 5:
                        A[i][j] = np.random.binomial(size = 1, n = 1, p = 0.6)
                else:
                    if j >= 10:
                        A[i][j] = np.random.binomial(size = 1, n = 1, p = 0.6)

        for i in range(15):
            A[i,i]=0
            for j in range(15):
                A[j][i] = A[i][j]
        NAs.append(A)
    return NAs
tenAs = getNAs(10)
