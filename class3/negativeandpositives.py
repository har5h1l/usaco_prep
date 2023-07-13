# https://codeforces.com/contest/1791/problem/E

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    negative = len([i for i in a if i < 0]) % 2
    
    b = sorted(list(map(abs, a)))
    print(sum(b) - min(b) * negative * 2)