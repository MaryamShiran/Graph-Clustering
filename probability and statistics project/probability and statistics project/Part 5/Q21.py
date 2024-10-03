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
            s += dist[i]

        return s

n = 1000
p = 0.0033
graph = Graph(n)

def generateGraph():
    for i in range(0, n-1):
        for j in range(i + 1, n):
            if(np.random.binomial(1, p, 1) == 1):
                graph.addEdge(i, j)

generateGraph()

distancesSum = 0
for i in range(0, n):
    distancesSum += graph.BFS(i)

print(distancesSum / (n * (n-1)))