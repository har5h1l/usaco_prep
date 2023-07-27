# https://codeforces.com/contest/1811/problem/A

for _ in range(int(input())):
    n, d = list(map(int, input().split*()))
    print(s:=input()[:(i:=sorted((s+d).split()).index(d))] + d * (n - len(s)) + s[i:])