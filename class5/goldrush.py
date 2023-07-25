# https://codeforces.com/contest/1829/problem/D

# if prime factorization of n has more 3s than it can be taken care of
# if it has more 2s it cannot
# if target has more 2s it can as long as the number of more 2s is lessthan or equal to the number of less 3s
# other prime factors have to be equal

def primefactorization(n):
    f = []
    
    i = 0
    while n % 2 == 0:
        n //= 2
        i += 1
    
    j = 0
    while n % 3 == 0:
        n //= 3
        j += 1

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
        f1, i1, j1 = primefactorization(n)
        f2, i2, j2 = primefactorization(m)

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