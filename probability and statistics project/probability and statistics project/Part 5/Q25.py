import numpy as np
import matplotlib.pyplot as plt

n = []
for i in range(0, 10):
    n.append((i + 1)*10)

repetations = 5
means = []

def mean(l):
    sum = 0
    for i in range(0, len(l)):
        sum += l[i]
    return sum / len(l)

def generateGraph(n, p):
    graph = [[0 for i in range(n)] for j in range(n)]
    for i in range(0, n-1):
        for j in range(i + 1, n):
            graph[i][j] = np.random.binomial(1, p, 1)[0]
            graph[j][i] = graph[i][j]
    return graph

for k in range(0, 10):
    transferProperties = []
    for i in range(0, repetations):
        graph = generateGraph(n[k], 60 / (n[k] * n[k]))
        graph = np.asarray(graph)
        graph2 = graph @ graph
        transfer = 0
        for i in range(0, n[k]):
            for j in range(0, n[k]):
                if(i != j):
                    if(graph2[i][j] > 0 and graph[i][j] > 0):
                        transfer += graph2[i][j]
        transferProperties.append(transfer / 6)
    means.append(mean(transferProperties))

plt.bar(n,means)
plt.show()








