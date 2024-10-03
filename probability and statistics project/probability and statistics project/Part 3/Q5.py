import numpy as np

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
        

z1 = np.array([3, 2, 1, 2, 2, 3, 1])
z2 = np.array([1, 3, 2, 3, 3, 1, 2])
print(d_H(z1, z2))


