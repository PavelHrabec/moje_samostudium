


import random

def roll(count, dice=10, modifier=0):# hodím 'count' kostek typu 'dice', sečtu a přičtu/odečtu modifier
    total = 0
    for _ in range(count):
        total += random.randint(1, dice)
        total += modifier
        return total






print(roll(2, 10, 5))  # hodí 2x 10-stěnnou a přičte 5





