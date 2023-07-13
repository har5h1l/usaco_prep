# http://usaco.org/index.php?page=viewproblem2&cpid=964

f = open('whereami.in').read().splitlines()
o = open('whereami.out', 'w')

n, colors = f
n = int(n)

for k in range(1, n+1):
    sequences = set()
    x = True

    for i in range(n-k+1):
        s = colors[i:i+k]
    
        if s in sequences:
            x = False
            break

        # else
        sequences.add(s)
    
    if x is True:
        o.write(str(k))
        break