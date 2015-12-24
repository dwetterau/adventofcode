__author__ = 'david'

world = []
file = open("input")
for line in file:
    world.append(list(line.strip()))

def valid(x, y):
    global world
    return x >= 0 and y >= 0 and x < len(world) and y < len(world)

def gol():
    global world
    new_world = [['.' for x in range(len(world))] for y in range(len(world))]
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(len(world)):
        for j in range(len(world)):
            count = 0
            for x in range(8):
                r, c = i + dr[x], j + dc[x]
                if valid(r, c):
                    if world[r][c] == "#":
                        count += 1
            if (i == 0 or i == 99) and (j == 0 or j == 99):
                new_world[i][j] = "#"
            if world[i][j] == "#":
                if 2 <= count <= 3:
                    new_world[i][j] = "#"
            else:
                if count == 3:
                    new_world[i][j] = "#"
    world = new_world

for i in range(100):
    gol()
print(sum(len([x for x in world[i] if x == "#"]) for i in range(len(world))))
