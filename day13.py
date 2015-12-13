__author__ = 'david'

from collections import defaultdict
from itertools import permutations

world = defaultdict(dict)
def apply_line(line):
    global world
    edges = line.split(" ")
    n1 = edges[0]
    n2 = edges[-1].strip()[:-1]

    distance = int(edges[3])
    if "lose" in edges:
        distance = -distance

    world[n1][n2] = distance

file = open("input")
total = 0
for line in file:
    apply_line(line)

all_paths = permutations(world.keys())
best_distance = 0
for path in all_paths:
    d = 0
    for i in range(len(path)):
        n1 = path[i]
        n2 = path[(i + 1) % len(path)]
        d += world[n1][n2]
        d += world[n2][n1]
    if d > best_distance:
        best_distance = d

print(best_distance)
