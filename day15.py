__author__ = 'david'

from collections import defaultdict
from itertools import permutations, combinations

num_types = 4
values = [[] for y in range(num_types)]
index = 0

def apply_line(line):
    global index
    line = line.strip().split()
    values[index] = [int(line[x][:-1]) for x in (2, 4, 6, 8, 10)]
    index += 1

file = open("input")
total = 0
for line in file:
    apply_line(line)

"""
# Lets try the DP approach
mat = [[(0, 0, 0, 0) for x in range(len(values) + 1)] for _ in range(101)]
for i in range(1, 101):
    for j in range(1, len(values) + 1):
        # Consider using exactly i ingredients, take the max of using the j - 1 one or the other max
        vals = [0] * 4
        prod = 1
        old_prod = 1
        for k in range(4):
            vals[k] = mat[i - 1][j][k] + values[j - 1][k]
            prod *= max(0, vals[k])
            old_prod *= max(0, mat[i][j - 1][k])
        print(i,j, prod, old_prod)
        if prod >= old_prod:
            mat[i][j] = tuple(vals)
        else:
            mat[i][j] = mat[i][j - 1]
"""

# Okay, lets try the combinatorics approach
r = range(100 + num_types - 1)
s = num_types
accum = [0, 0, 0, 0, 0]
best = 0
c = 0
for indices in combinations(r, s - 1):
    # The indices tell us where the dividers of the bins are
    c += 1
    if (c % 10) == 0:
        print(c)
    cur = 0
    i = 0
    while i < 5:
        accum[i] = 0
        i += 1
    for j in r:
        if cur >= s - 1:
            i = 0
            while i < 5:
                accum[i] += values[-1][i]
                i += 1
        elif j < indices[cur]:
            i = 0
            while i < 5:
                accum[i] += values[cur][i]
                i += 1
        elif j == indices[cur]:
            cur += 1
    if accum[-1] != 500:
        continue
    i = 0
    prod = 1
    while i < 4:
        prod *= max(0, accum[i])
        i += 1
    best = max(best, prod)

print(best)
