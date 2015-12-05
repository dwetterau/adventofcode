__author__ = 'david'

from hashlib import md5

# puzzle = "yzbqklnj".encode('utf-8')

x = 0
while True:
    m = md5()
    puzzle = ("yzbqklnj%s" % x).encode('utf-8')
    m.update(puzzle)
    h = m.hexdigest()
    if h.startswith("000000"):
        print(x)
        break
    x += 1
    if x % 1000000 == 0:
        print("Working on... %s" % x)
