import numpy as np

counts = []
n = 1000
p = 0.0034
repetations = 10

def mean(l):
    sum = 0
    for i in range(0, len(l)):
        sum += l[i]
    return sum / len(l)


for i in range(0, repetations):
    counts.append(sum(np.random.binomial(1, p, n*(n-1)//2)))

print(counts)
print(mean(counts))