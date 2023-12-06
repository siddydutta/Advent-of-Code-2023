from functools import reduce
from operator import mul

file = open('input.txt')
data = file.read()
file.close()

times = list(map(int, data.split('\n')[0].split()[1:]))
distances = list(map(int, data.split('\n')[1].split()[1:]))

n_ways = []
for time, distance in zip(times, distances):
    options = 0
    for i in range(0, time+1):
        d = i * (time - i)
        if d > distance:
            options += 1
    n_ways.append(options)
    
print(reduce(mul, n_ways))
