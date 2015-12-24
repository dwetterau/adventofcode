from collections import defaultdict

__author__ = 'david'

x = [0 for _ in range(3600000)]
for i in range(1, len(x)):
    j = i
    c = 0
    while j < len(x) and c < 50:
        x[j] += i * 11
        j += i
        c += 1

for i in range(0, len(x)):
    if x[i] > 36000000:
        print(i)
        break
print max(x)

