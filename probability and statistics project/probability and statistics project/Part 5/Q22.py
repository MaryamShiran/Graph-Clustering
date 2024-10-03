import numpy as np

class Graph:
     
    adj = []

    def __init__(self, v):
         
        self.v = v
        Graph.adj = [[0 for i in range(v)]
                        for j in range(v)]
 
    def addEdge(self, start, e):
        Graph.adj[start][e] = 1
        Graph.adj[e][start] = 1
 
    def BFS(self, start):
        s = 0
        visited = [False] * self.v
        q = [start]
        visited[start] = True
        dist = visited = [0] * self.v
 
        while q:
            vis = q[0]
            q.pop(0)
            
            for i in range(self.v):
                if (Graph.adj[vis][i] == 1 and
                      (not visited[i])):
                    q.append(i)
                    visited[i] = True
                    dist[i] = dist[vis] + 1
                    
        for i in range(0, n):
            if(dist[i] > s):
                s = dist[i]

        return s

n = 50
p = 0.34
repetations = 100
maxDistances = []

def generateGraph(graph):
    for i in range(0, n-1):
        for j in range(i + 1, n):
            if(np.random.binomial(1, p, 1) == 1):
                graph.addEdge(i, j)

def mean(l):
    sum = 0
    for i in range(0, len(l)):
        sum += l[i]
    return sum / len(l)

for i in range(0, repetations):
    graph = Graph(n)
    generateGraph(graph)
    max = 0
    for j in range(0, n):
        dist = graph.BFS(j)
        if(max < dist):
            max = dist
    maxDistances.append(max)

print(mean(maxDistances))
    

    


