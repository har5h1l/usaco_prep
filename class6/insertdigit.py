# https://codeforces.com/contest/1811/problem/A

for _ in range(int(input())):
    n, d = input().split()
    s = input().split()
    x = int(n) - len(s) # number of additional digits

    if x > 0:
        for i in range(int(n)): 
            if s[i] < d: s.insert(i, d * x)
    
    print(''.join(s))