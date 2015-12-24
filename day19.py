from collections import defaultdict

__author__ = 'david'

mappings = [
('Al', 'ThF'),
('Al', 'ThRnFAr'),
('B', 'BCa'),
('B', 'TiB'),
('B', 'TiRnFAr'),
('Ca', 'CaCa'),
('Ca', 'PB'),
('Ca', 'PRnFAr'),
('Ca', 'SiRnFYFAr'),
('Ca', 'SiRnMgAr'),
('Ca', 'SiTh'),
('F', 'CaF'),
('F', 'PMg'),
('F', 'SiAl'),
('H', 'CRnAlAr'),
('H', 'CRnFYFYFAr'),
('H', 'CRnFYMgAr'),
('H', 'CRnMgYFAr'),
('H', 'HCa'),
('H', 'NRnFYFAr'),
('H', 'NRnMgAr'),
('H', 'NTh'),
('H', 'OB'),
('H', 'ORnFAr'),
('Mg', 'BF'),
('Mg', 'TiMg'),
('N', 'CRnFAr'),
('N', 'HSi'),
('O', 'CRnFYFAr'),
('O', 'CRnMgAr'),
('O', 'HP'),
('O', 'NRnFAr'),
('O', 'OTi'),
('P', 'CaP'),
('P', 'PTi'),
('P', 'SiRnFAr'),
('Si', 'CaSi'),
('Th', 'ThCa'),
('Ti', 'BP'),
('Ti', 'TiTi'),
('e', 'HF'),
('e', 'NAl'),
('e', 'OMg'),
]
#string = "HOHOHO"
string = "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"

counts = {}
for x in mappings:
    if x[0] not in counts:
        counts[x[0]] = []
    counts[x[0]].append(x[1])

def combs_easy(inp, i, done=False):
    global counts, mappings
    if done and i == len(inp):
        return [""]
    elif i == len(inp):
        return []
    a = set()
    if i < len(inp) - 1:
        # Try the two letter case too
        if not done and inp[i:i + 2] in counts:
            ways = combs_easy(inp, i + 2, True)
            for way in ways:
                for this in counts[inp[i:i + 2]]:
                    a.add("".join([this] + list(way)))

    # Try the one letter case
    if not done and inp[i:i + 1] in counts:
        ways = combs_easy(inp, i + 1, True)
        for way in ways:
            for this in counts[inp[i:i + 1]]:
                a.add("".join([this] + list(way)))

    # Try not substituting
    ways = combs_easy(inp, i + 1, done)
    for way in ways:
        a.add("".join([inp[i:i + 1]] + list(way)))
    return list(a)

#string = "HOHOHO"
#mappings = [('e', 'H'), ('e', 'O'), ('H', 'HO'), ('H', 'OH'), ('O', 'HH')]
# HOHOHO -> 6
# HOH -> 3
def generate(l, depth=0):
    global mappings
    if l == ['e']:
        return depth
    # For each rule, try to apply it
    attempts = []
    potential_subs = []

    for lhs, rhs in mappings:
        for i in range(0, len(l)):
            if list(rhs) == l[i:i + len(rhs)]:
                potential_subs.append(l[0:i] + list(lhs) + l[i + len(rhs):])
    # Only recurse on like.. the best 1 subs?
    potential_subs.sort(key=lambda x: len(x))
    for sub in potential_subs[:1]:
        attempts.append(generate(sub, depth + 1))

    # Return the best
    if not attempts:
        return 10000000
    return min(attempts)

# Possible answers:
# - 212 (full greedy)
# - XXX (try best 2)


print(generate(list(string)))