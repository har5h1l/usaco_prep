# https://codeforces.com/contest/1811/problem/B

def conveyor(x, y, n):
    for i in range(1, int(n/2 + 1)):
        if x in (i, n-i+1): return i
        elif y in (i, n-i+1): return i

for _ in range(int(input())):
    n, x1, y1, x2, y2 = list(map(int, input().split()))
    print(abs(conveyor(x1, y1, n) - conveyor(x2, y2, n)))