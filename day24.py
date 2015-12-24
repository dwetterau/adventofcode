import itertools
weights = [1, 2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 53, 59, 61, 67, 71, 73, 79, 83, 89,
           97, 101, 103, 107, 109, 113]

l = None
total = sum(weights)
prods = []
for i in range(1, 7):
    for x in itertools.combinations(weights, i):
        t = sum(x)
        if t == total / 3:  # put 4 here for part 2
            prods.append(reduce(lambda _x, _y: _x * _y, x))
    if prods:
        print min(prods)
        break
