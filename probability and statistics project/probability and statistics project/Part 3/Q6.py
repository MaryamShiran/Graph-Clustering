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

def manfi_log_likelihood_A(A, z):
    likelihood = 0
    for i in range(15):
        for j in range(i + 1, 15):
            if z[i] == z[j]:
                if A[i, j] == 0:
                    likelihood += np.log(0.4)
                if A[i, j] == 1:
                    likelihood += np.log(0.6)
            if z[i] != z[j]:
                if A[i, j] == 0:
                    likelihood += np.log(0.9)
                if A[i, j] == 1:
                    likelihood += np.log(0.1)
    return likelihood * (-1)
A = getNAs(1)[0]
z0 = np.array([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3])

np.random.shuffle(z0)
print(manfi_log_likelihood_A(A, z0))

