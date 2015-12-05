__author__ = 'david'

def nice(string):
    num_vowels = sum(1 for x in string if x in {"a", "e", "i", "o", "u"})
    if num_vowels < 3:
        return False

    for bad in ["ab", "cd", "pq", "xy"]:
        if bad in string:
            return False

    for index in range(1, len(string)):
        if string[index] == string[index - 1]:
            return True
    return False

assert nice("ugknbfddgicrmopn")
assert nice("aaa")
assert not nice("jchzalrnumimnmhp")
assert not nice("haegwjzuvuyypxyu")
assert not nice("dvszwmarrgswjxmb")

def nice2(string):
    found_non_overlapping_pair = False
    for i in (range(1, len(string))):
        for j in range(i + 2, len(string)):
            if string[i - 1:i + 1] == string[j - 1:j + 1]:
                found_non_overlapping_pair = True
                break
        if found_non_overlapping_pair:
            break
    if not found_non_overlapping_pair:
        return False

    for i in range(2, len(string)):
        if string[i - 2] == string[i]:
            return True
    return False

assert nice2("qjhvhtzxzqqjkmpb")
assert nice2("xxyxx")
assert nice2("xxxx")
assert not nice2("uurcxstgmygtbstg")
assert not nice2("ieodomkazucvgmuy")

file = open("input")
total = 0
for line in file:
    if nice2(line):
        total += 1
print(total)
