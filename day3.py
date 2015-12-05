__author__ = 'david'

def distinct(string):
    visited = dict()
    position = (0, 0)
    map = {"v": (0, -1), "^": (0, 1), "<": (-1, 0), ">": (1, 0)}
    visited[position] = True
    for char in string:
        delta = map[char]
        position = position[0] + delta[0], position[1] + delta[1]
        visited[position] = True
    return len(visited)

print(distinct(">"))
print(distinct("^>v<"))
print(distinct("^v^v^v^v^v"))

def distinct2(string):
    visited = dict()
    positions = [(0, 0), (0, 0)]
    map = {"v": (0, -1), "^": (0, 1), "<": (-1, 0), ">": (1, 0)}
    visited[positions[0]] = True
    for index, char in enumerate(string):
        delta = map[char]
        which = index % 2
        positions[which] = positions[which][0] + delta[0], positions[which][1] + delta[1]
        visited[positions[which]] = True
    return len(visited)

print(distinct2("^v"))
print(distinct2("^>v<"))
print(distinct2("^v^v^v^v^v"))

file = open("input")
total = 0
for line in file:
    total += distinct2(line)
print(total)
