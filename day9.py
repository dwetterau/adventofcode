__author__ = 'david'

from collections import defaultdict
from itertools import product

world = defaultdict(dict)
def apply_line(line):
    global world
    edges = line.split(" ")
    n1 = edges[0]
    n2 = edges[2]
    distance = int(edges[-1])
    world[n1][n2] = distance
    world[n2][n1] = distance

file = open("input")
total = 0
for line in file:
    apply_line(line)

all_paths = product(*[list(world.keys())] * len(world))
best_distance = 0
for path in all_paths:
    d = 0
    visited = {path[0]}
    for i in range(1, len(path)):
        n1, n2 = path[i - 1:i + 1]
        if n2 in visited:
            d = best_distance
            break
        visited.add(n2)
        if n2 not in world[n1]:
            # Invalid edge, break out
            d = best_distance
            break
        d += world[n1][n2]
    if d > best_distance:
        best_distance = d

print(best_distance)
