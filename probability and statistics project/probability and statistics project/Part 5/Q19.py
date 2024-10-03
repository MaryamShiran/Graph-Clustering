import numpy as np

n = 3000
p = 0.01
repetations = 5

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
chainProperties = []

for i in range(0, repetations):
    graph = generateGraph()
    graph = np.asarray(graph)
    graph2 = graph @ graph
    transfer = 0
    chain = 0
    for i in range(0, n):
        for j in range(0, n):
            if(i != j):
                if(graph2[i][j] > 0 and graph[i][j] > 0):
                    transfer += graph2[i][j]
                elif(graph2[i][j] > 0):
                    chain += graph2[i][j]
    transferProperties.append(transfer / 6)
    chainProperties.append(chain / 2)

print(mean(transferProperties))
print(mean(chainProperties))
