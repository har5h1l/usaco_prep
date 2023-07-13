# http://www.usaco.org/index.php?page=viewproblem2&cpid=963

f = open('gymnastics.in')
o = open('gymnastics.out', "w")

k, n = list(map(int, f.readline().split()))
rankings = [list(map(int, r.split())) for r in f.read().splitlines()]

out = 0

for i in range(1, n + 1):
    for x in range(1, n+1):
        if i == x:
            continue

        c = True

        for r in rankings:
            if r.index(i) < r.index(x):
                c = False
                break

        if c == True:
            out += 1

o.write(str(out))