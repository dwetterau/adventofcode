__author__ = 'david'

from collections import defaultdict
from itertools import permutations

# Map from Name to tuple of speed, good_time, wait time
deer = dict()

# Map from Name to (current position, state, time left)
position = dict()

def apply_line(line):
    global deer, position
    line = line.strip().split()
    name, speed, good, wait = line[0], int(line[3]), int(line[6]), int(line[-2])
    deer[name] = (speed, good, wait)
    position[name] = (0, True, good)

file = open("input")
total = 0
for line in file:
    apply_line(line)

winners = defaultdict(int)
for i in range(2503):
    for d, t in position.items():
        speed, good, wait = deer[d]

        new_t = list(t)
        if t[1]:
            # We are flying
            new_t[0] = t[0] + speed
        new_t[2] -= 1
        if not new_t[2]:
            if t[1]:
                # We will now rest
                new_t[1] = False
                new_t[2] = wait
            else:
                new_t[1] = True
                new_t[2] = good
        position[d] = tuple(new_t)

    best = max(tup[0] for tup in position.values())
    for d, t in position.items():
        if t[0] == best:
            winners[d] += 1

print(max(winners.values()))
