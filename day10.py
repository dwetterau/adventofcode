__author__ = 'david'

from collections import defaultdict
from itertools import product

world = defaultdict(dict)

def apply(s):
    cur = None
    count = 0
    n = ""
    for i in range(len(s)):
        if s[i] != cur:
            if cur is not None:
                n += "%s%s" % (count, cur)
            cur = s[i]
            count = 1
        else:
            count += 1
    n += "%s%s" % (count, cur)
    return n

v = "1113122113"
#v = "1"
for i in range(50):
    v = apply(v)
print(len(v))
