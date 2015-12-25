__author__ = 'david'
from collections import defaultdict

world = defaultdict(dict)
world[1][1] = 20151125
last = world[1][1]
for diagonal in range(2, 6056):
    r = diagonal
    c = 1
    while c < diagonal + 1:
        world[r][c] = (last * 252533) % 33554393
        last = world[r][c]
        if r == 2981 and c == 3075:
            print last
        r -= 1
        c += 1

