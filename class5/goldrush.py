# https://codeforces.com/contest/1829/problem/D

def primecounts(n):
    f = []
    
    # number of 2s as factor
    i = 0
    while n % 2 == 0:
        n //= 2
        i += 1
    
    # number of 3s as factor
    j = 0
    while n % 3 == 0:
        n //= 3
        j += 1

    # other prime factors
    d = 5
    while n != 1 and d <= n:
        if n % d == 0:
            f.append(d)
            n //= d
        else: d += 2

    return f, i, j
 
for _ in range(int(input())):
    n, m = list(map(int, input().split())) # n = start; m = target
 
    if n > m:
        f1, i1, j1 = primecounts(n)
        f2, i2, j2 = primecounts(m)

        if i1 > i2: print('NO')

        else:
            if j1 - j2 < i2 - i1: print('NO')
            else:
                if f1 == f2: print('YES')
                else: print('NO')

    elif n < m:
        print('NO')

    else:
        print('YES')