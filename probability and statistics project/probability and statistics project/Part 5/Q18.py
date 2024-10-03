import numpy as np
import matplotlib.pyplot as plt

sameColorsCount = []
n = 1000
p = 0.00016
repetations = 10

x= []
for i in range(0, n):
    x.append(i)
y = [0 for i in range(n)]

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

def calculateAverageDegree(graph):
    s = 0
    for i in range(0, n):
        c = sum(graph[i])
        s += c
        y[int(c)] += 1
    return s / n

def countSameColors(graph, l):
    count = 0
    for i in range(0, n):
        if(sum(graph[i]) > l):
            count+=1
    return count

for i in range(0, repetations):
    graph = generateGraph()
    l = calculateAverageDegree(graph)
    sameColorsCount.append(countSameColors(graph, l))

print(mean(sameColorsCount))

for i in range(n):
    y[i] /= repetations

plt.bar(x, y)
plt.show()



