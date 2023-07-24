# https://codeforces.com/contest/1829/problem/B

for _ in range(int(input())):
    n = int(input())
    t = ' ' + ''.join(input().split())

    b = '0' * n
    out = 0
    while len(b) > 0:
        if b in t:
            out = len(b)
            break
        b = b[:-1]

    print(out)