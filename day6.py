__author__ = 'david'

def op_and_coords(line):
    op = "toggle",
    if "on" in line:
        op = "on",
    elif "off" in line:
        op = "off",

    coords = line.split(" through ")
    coord1 = coords[0].split(" ")[-1]
    coord2 = coords[1]

    s_to_tup = lambda c: tuple(int(x) for x in c.split(","))

    return op, s_to_tup(coord1), s_to_tup(coord2)

world = [[0 for x in range(1000)] for y in range(1000)]
def apply_line(line):
    global world
    op, coord1, coord2 = op_and_coords(line)
    for x in range(coord1[0], coord2[0] + 1):
        for y in range(coord1[1], coord2[1] + 1):
            if op == "toggle":
                world[x][y] = (world[x][y] + 2)
            elif op == "on":
                world[x][y] += 1
            elif op == "off":
                world[x][y] = max(0, world[x][y] - 1)




file = open("input")
total = 0
for line in file:
    apply_line(line)

print(sum(sum(x) for x in world))
