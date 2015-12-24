from collections import defaultdict

__author__ = 'david'

sues = defaultdict(dict)
def apply_line(line):
    global sues
    line = line.strip().split()
    sues[line[1][:-1]][line[2][:-1]] = int(line[3][:-1])
    sues[line[1][:-1]][line[4][:-1]] = int(line[5][:-1])
    sues[line[1][:-1]][line[6][:-1]] = int(line[7])

file = open("input")
total = 0
for line in file:
    apply_line(line)

readings = dict(
    children=3,
    cats=7,
    samoyeds=2,
    pomeranians=3,
    akitas=0,
    vizslas=0,
    goldfish=5,
    trees=3,
    cars=2,
    perfumes=1,
)
for sue, r in sues.items():
    bad = False
    for k, v in r.items():
        if k in {"cats", "trees"} and v <= readings[k]:
            bad = True
        elif k in {"pomeranians", "goldfish"} and v >= readings[k]:
            bad = True
        elif k not in {"cats", "trees", "pomeranians", "goldfish"} and v != readings[k]:
            bad = True
    if not bad:
        print(sue)
        break
