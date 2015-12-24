from collections import defaultdict

import itertools

__author__ = 'david'

spells = [
    # mana, damage, heal, shield, att, mana, duration
    (53, 4, 0, 0, 0, 0, 0),
    (73, 2, 2, 0, 0, 0, 0),
    (113, 0, 0, 7, 0, 0, 6),
    (173, 0, 0, 0, 3, 0, 6),
    (229, 0, 0, 0, 0, 101, 5)
]

best = 1000000000000
def iterate(total, depth, timers, mana, shield, health, ehealth):
    global spells, best, edamage
    # See if we're dead
    if health <= 0:
        return
    elif ehealth <= 0:
        # We won! see if the mana cost was good
        if total < best:
            best = total
        return

    # Process the timers
    for k, v in timers.items():
        if k[4]:
            ehealth -= k[4]
        elif k[3] and v == 0:
            shield -= k[3]
        elif k[5]:
            mana += k[5]

    # Get rid of all the expired timers
    timers = {k: v - 1 for k, v in timers.items() if v > 0}

    # See if anyone died
    if ehealth <= 0:
        # We won! see if the mana cost was good
        if total < best:
            best = total
        return

    if depth % 2 == 0:
        # Hard mode, we lose a health
        health -= 1
        if health <= 0:
            return

        # Figure out the valid spells
        valid = [s for s in spells if s not in timers and s[0] <= mana]
        for s in valid:
            # Try casting each spell
            ntimers = {k: v for k, v in timers.items()}
            if not s[-1]:
                # instant spell
                nehealth = ehealth - s[1]
                nhealth = health + s[2]
                nshield = shield
            else:
                nehealth = ehealth
                nhealth = health
                nshield = shield + s[3]
                ntimers[s] = s[-1] - 1
            # print "CASTING:", s
            iterate(total + s[0], depth + 1, ntimers, mana - s[0], nshield, nhealth, nehealth)
    else:
        # The boss goes, inflict the damage
        health -= max(1, edamage - shield)
        iterate(total, depth + 1, timers, mana, shield, health, ehealth)
edamage = 10
iterate(0, 0, {}, mana=500, shield=0, health=50, ehealth=71)
print best
