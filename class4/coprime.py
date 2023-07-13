# https://codeforces.com/contest/1742/problem/D

from math import gcd

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    out = -1

    lastindex = [-1 for _ in range(1001)]
    for i in range(n): lastindex[a[i]] = i + 1
    
    for i in range(1, 1001):
        for j in range(1, 1001):
            
            if gcd(i, j) != 1: continue
            if lastindex[i] == -1 or lastindex[j] == -1: continue
            out = max(out, lastindex[i] + lastindex[j])
    
    print(out)

