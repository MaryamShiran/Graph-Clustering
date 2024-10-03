import numpy as np

n = 1000
p = 0.003
repeteations = 100

def mean(l):
    sum = 0
    for i in range(0, len(l)):
        sum += l[i]
    return sum / len(l)

def generateGraph():
    graph = [[0 for i in range(n)] for j in range(n)]
    for i in range(0, n-1):
        for j in range(i + 1, n):
            graph[i][j] = np.random.binomial(1, p, 1)
            graph[j][i] = graph[i][j]
    return graph

counts = []
for k in range(0, repeteations):

    graph = generateGraph()

    l = []
    for i in range(0, n):
        if(graph[0][i]==1):
            l.append(i)

    count = 0
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if(graph[i][j]==1):
                count+=1
    counts.append(count)

print(mean(counts))









