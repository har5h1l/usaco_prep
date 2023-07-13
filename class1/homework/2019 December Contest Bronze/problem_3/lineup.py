# http://usaco.org/index.php?page=viewproblem2&cpid=965

from itertools import permutations

f = open('lineup.in').read().splitlines()
o = open('lineup.out', 'w')

n = f[0]
c = [(i.split()[0], i.split()[-1]) for i in f[1:]]

orders = list(permutations(['Beatrice', 'Belinda', 'Bella', 'Bessie', 'Betsy', 'Blue', 'Buttercup', 'Sue']))

for order in orders:
    t = True
    for constraint in c:
        if abs(order.index(constraint[0]) - order.index(constraint[1])) != 1:
            t = False
            break
    if t:
        for cow in order:
            o.write(cow + '\n')
        break
