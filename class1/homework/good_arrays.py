# https://codeforces.com/problemset/problem/1777/A

for _ in range(int(input())):
    n = int(input())
    a = [int(i) % 2 for i in input().split()]
    out = 0

    for i in range(n-1):
        if a[i] == a[i+1]:
            out += 1

    print(out)