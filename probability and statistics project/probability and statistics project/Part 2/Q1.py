import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import math

def probability (u, v, F):
    tmp = 0.0
    C = F.shape[1]
    for c in range(C):
        tmp += F[u, c] * F[v, c]
    tmp = 1- math.exp(-tmp)
    return tmp

def d_probability(u, v, C, F):
    ans = probability(u, v, F)
    return F[v, C] * (1 - ans)

def log_likelihood(F, A):
    n = A.shape[0]
    C = F.shape[1]
    log_likelihood = 0.0
    for i in range(n):
        for j in range(n):
            if(A[i, j] == 1):
                log_likelihood += math.log(probability(i, j, F))
            else:
                log_likelihood += math.log(1.001 - probability(i, j, F))
    return log_likelihood

def gradient(F, A, u):
    n = A.shape[0]
    C = F.shape[1]
    gradient = []
    for c in range(C):
        ans = 0.0
        for j in range(n):
            if(j != u):
                tmp = 0.1
            if(A[u, j] == 1):
                tmp = d_probability(u, j, c, F) / probability(j, u, F)
            else:
                tmp = d_probability(j, j, c, F) / (1 - probability(j, u, F))
            ans += tmp
            gradient.append(ans)
    return gradient


def train(A, C, iterations = 200):
    N = A.shape[0]
    F = np.random.rand(N, C)
    for n in range(iterations):
        for person in range(N):
            grad = gradient(F, A, person)
            F[person] += 0.005 * np.reshape(grad, -1)
            F[person] = np.maximum(0.001, F[person])
        ll = log_likelihood(F, A)
    return F

A = np.random.rand(40, 80)
A[0:15, 0:25] = A[0:15, 0:25] > 1 - 0.6
A[0:15, 25:40] = A[0:15, 25:40] > 1 - 0.1
A[15:40, 25:40] = A[15:40, 25:40] > 1 - 0.7
A[15:25, 15:25] = A[15:25, 15:25] > 1 - 0.8
for i in range(40):
    A[i, i] = 0
    for j in range(i):
        A[i, j] = A[j, i]
delta = np.sqrt(-np.log(1-0.1))
F = train(A, 2, iterations=120)
G = nx.from_numpy_array(A)
C = F > delta
nx.draw(G, node_color = 10*(C[:,0])+20*(C[:,1]))
