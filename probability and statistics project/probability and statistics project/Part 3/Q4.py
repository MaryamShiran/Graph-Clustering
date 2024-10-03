import numpy as np

def d(z1, z2):
    acc = 0
    for i in range(len(z1)):
        if z1[i] != z2[i]:
            acc += 1
    return acc

z1 = np.array([1, 1, 2, 3, 2, 3, 2, 2, 3, 1, 1, 1, 2, 3, 3])
z2 = np.array([1, 2, 3, 3, 2, 3, 2, 2, 3, 1, 1, 1, 1, 3, 3])
print(d(z1, z2))
