__author__ = 'david'

sizes = sorted([ 33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42])


def nog(n, index=len(sizes) - 1):
    global sizes
    if n == 0:
        return [[]]
    elif n < 0 or index < 0:
        return []
    cur = sizes[index]
    cur_sum = 0
    cur_times = 0
    cur_ways = []
    while cur_sum <= n:
        ways = nog(n - cur_sum, index - 1)
        for way in ways:
            cur_ways.append([cur] * cur_times + way)
        cur_times += 1
        cur_sum += cur
        if cur_times == 2:
            break
    return cur_ways

x = nog(150)
z = min(len(y) for y in x)
print(len([y for y in x if len(y) == z]))
