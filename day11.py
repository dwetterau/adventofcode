__author__ = 'david'

from collections import defaultdict
from itertools import product

world = defaultdict(dict)

as_num = lambda x: ord(x) - 97
to_char = lambda x: chr(x + 97)


def check(string):
    for x in string:
        if x in {'i', 'o', 'l'}:
            return False

    check1, check2, check3 = [False] * 3
    for i in range(2, len(string)):
        if as_num(string[i]) - as_num(string[i - 1]) == 1 and (
                as_num(string[i - 1]) - as_num(string[i - 2]) == 1):
            check1 = True
    if not check1:
        return False
    i = 1
    while i < len(string):
        if string[i] == string[i - 1]:
            if check2:
                check3 = True
            else:
                check2 = True
                i += 1
        i += 1
    return all((check2, check3))


assert not check('hijklmn')
assert not check('abbceffg')
assert not check('abbcegjk')
assert check('abccee')

def n(string):
    s_array = list(string)
    def incr():
        i = len(string) - 1
        while i >= 0:
            # Run the increment
            n = as_num(s_array[i])
            if n == 25:
                # We must carry
                s_array[i] = "a"
                i -= 1
            else:
                s_array[i] = to_char(n + 1)
                return

    # incr once
    incr()
    while not check(s_array):
        incr()

    return "".join(s_array)

assert n('abcdefgh') == 'abcdffaa', n('abcdefgh')
assert n('ghijklmn') == 'ghjaabcc'

# v = 'hepxcrrq'
v = 'hepxxyzz'
print(n(v))
