import numpy as np
import matplotlib.pyplot as plt

def getAByZ(z):
    A = np.random.binomial(size = (15, 15), n = 1, p = 0.1)
    for i in range(15):
        for j in range(15):
            if z[i] == z[j]:
                A[i][j] = np.random.binomial(size = 1, n = 1, p = 0.6)
    
    for i in range(15):
        A[i,i]=0
        for j in range(15):
            A[j][i] = A[i][j]
    return A
def permutation_helper(O, cur, nex):
    
    if len(nex) == 0:
        O.append(cur)
    for i in range(len(nex)):
        cur2 = cur.copy()
        cur2.append(nex[i])
        nex2 = nex.copy()
        del nex2[i]
        permutation_helper(O, cur2, nex2)
def permutation(n):
    a = []
    cur = []
    nex = []
    for i in range(1, n + 1):
        nex.append(i)
    permutation_helper(a, cur, nex)
    return a

def mapper(z, permutation):
    new_z = []
    for i in range(len(z)):
        new_z.append(permutation[z[i] - 1])
    return np.array(new_z)
def d(z1, z2):
    acc = 0
    for i in range(len(z1)):
        if z1[i] != z2[i]:
            acc += 1
    return acc

def d_H(z1, z2):
    all_permutations = permutation(3)
    ds = []
    for p in all_permutations:
        ds.append(d(z1, mapper(z2, p)))
    return min(ds)
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

def train(A, z0, T):
    likelihoods = []
    distances = []
    reference_z = z0.copy()
    z = z0
    for t in range(T):
        i_best = 0
        j_best = 0
        likelihood_best = manfi_log_likelihood_A(A, z0)
        for i in range(15):
            for j in range(15):
                z_test = z.copy()
                c = z_test[i]
                z_test[i] = z_test[j]
                z_test[j] = c
                cur_likelihood = manfi_log_likelihood_A(A, z_test)
                if cur_likelihood < likelihood_best:
                    i_best = i
                    j_best = j
                    best_likelihood_A = cur_likelihood
        c = z[i_best]
        z[i_best] = z[j_best]
        z[j_best] = c
        likelihoods.append(likelihood_best)
        distances.append(d_H(z, reference_z))
    result = [likelihoods, distances]
    return result
        
        
                
                
z0 = np.array([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3])
A = getAByZ(z0)
print("real z: ", z0)
for i in range(10):
    print("n = ", i + 1)
    np.random.shuffle(z0)
    print("first_z : ", z0)
    train(A, z0, 20)
    print("last_z : ", z0)
    