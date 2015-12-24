__author__ = 'david'

def area(string):
    sizes = [int(x) for x in string.split("x")]
    areas = [sizes[0] * sizes[1], sizes[1] * sizes[2], sizes[2] * sizes[0]]
    min_side = min(areas)
    return min_side + sum(2 * x for x in areas)

print(area("2x3x4"))
print(area("1x1x10"))

def ribbon(string):
    sizes = [int(x) for x in string.split("x")]
    perimeter = [sizes[0] + sizes[1], sizes[1] + sizes[2], sizes[2] + sizes[0]]
    min_perimeter = 2 * min(perimeter)
    volume = sizes[0] * sizes[1] * sizes[2]
    return min_perimeter + volume

print(ribbon("2x3x4"))
print(ribbon("1x1x10"))

file = open("input")
total = 0
for line in file:
    total += ribbon(line)
print(total)
