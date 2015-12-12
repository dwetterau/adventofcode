__author__ = 'david'

import json

def parse_element(x):
    if isinstance(x, dict):
        return parse_object(x)
    elif isinstance(x, list):
        return parse_array(x)
    elif isinstance(x, int):
        return x
    else:
        return 0

def parse_object(a):
    sum = 0
    # Step 2 modification
    for x in a.values():
        if x == "red":
            return 0
    # end of modification
    for x in a.values():
        sum += parse_element(x)
    return sum

def parse_array(a):
    sum = 0
    for x in a:
        sum += parse_element(x)
    return sum

def test(x, expected):
    x = json.loads(x)
    s = parse_element(x)
    assert s == expected, s

test('[{"a":2,"b":4}, [1,2,3]]', 12)
test('[[[3]], {"a": [-1, 1]}]', 3)

file = open("input")
total = 0
for line in file:
    print(parse_element(json.loads(line)))
