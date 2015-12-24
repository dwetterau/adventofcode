import itertools

__author__ = 'david'

weapons = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0),
]

armor = [
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
    (0, 0, 0),  # Not buying any
]

rings = [
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
    (0, 0, 0),  # Not buying any
    (0, 0, 0, 0),
]

best = 10000
best2 = 0
for items in itertools.product(weapons, armor, rings, rings):
    # Can't buy the same ring twice
    if items[2] == items[3]:
        continue

    cost, my_d, my_a = (sum(item[i] for item in items) for i in range(3))
    my_health = 100
    enemy_d, enemy_a, enemy_health = 8, 2, 100
    turn = 0
    while my_health > 0 and enemy_health > 0:
        if turn % 2:
            my_health -= max(1, enemy_d - my_a)
        else:
            enemy_health -= max(1, my_d - enemy_a)
        turn += 1
    if my_health > 0 and cost < best:
        best = cost
    if my_health <= 0 and cost > best2:
        best2 = cost
print best, best2

