# https://codeforces.com/contest/1791/problem/D

for _ in range(int(input())):
    n = int(input())
    x = input() # s

    pl, sl = [], []
    p, s = set(), set()

    for i in range(n-1):
        p.add(x[i])
        s.add(x[n-i-1])

        pl.append(len(p))
        sl.append(len(s))
    
    sl = sl[::-1]
    
    print(max(i + j for i, j in zip(pl, sl)))