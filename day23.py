from collections import defaultdict

import itertools

__author__ = 'david'

program = []

def apply(line):
    global program
    line = line.strip().split()
    if line[0] == 'jio':
        program.append(("jio", line[1][:-1], int(line[2])))
    elif line[0] == 'jie':
        program.append((line[0], line[1][:-1], int(line[2])))
    elif line[0] == 'jmp':
        program.append((line[0], None, int(line[1])))
    else:
        program.append((line[0], line[1]))
file = open("input")
for line in file:
    apply(line)

registers = {"a": 1, "b": 0}
index = 0
while index < len(program):
    op = program[index]
    if op[0] in {"hlf", "tpl", "inc"}:
        if op[0] == "hlf":
            registers[op[1]] /= 2
        elif op[0] == "tpl":
            registers[op[1]] *= 3
        elif op[0] == "inc":
            registers[op[1]] += 1
        index += 1
    else:
        if op[0] == "jio":
            if registers[op[1]] == 1:
                index += op[2]
            else:
                index += 1
        elif op[0] == "jie":
            if registers[op[1]] % 2 == 0:
                index += op[2]
            else:
                index += 1
        else:
            index += op[2]
print registers["b"]