import numpy as np

n = 100
p = 0.34
repetations = 100

def mean(l):
    sum = 0
    for i in range(0, len(l)):
        sum += l[i]
    return sum / len(l)

def generateGraph():
    graph = [[0 for i in range(n)] for j in range(n)]
    for i in range(0, n-1):
        for j in range(i + 1, n):
            graph[i][j] = np.random.binomial(1, p, 1)[0]
            graph[j][i] = graph[i][j]
    return graph

transferProperties = []

for i in range(0, repetations):
    graph = generateGraph()
    graph = np.asarray(graph)
    graph2 = graph @ graph
    transfer = 0
    for i in range(0, n):
        for j in range(0, n):
            if(i != j):
                if(graph2[i][j] > 0 and graph[i][j] > 0):
                    transfer += graph2[i][j]
    transferProperties.append(transfer / 6)

print(mean(transferProperties))








