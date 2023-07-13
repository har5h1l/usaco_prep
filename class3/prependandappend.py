# https://codeforces.com/contest/1791/problem/C

for _ in range(int(input())):
    _ = input()
    s = input()

    while s[0] != s[-1]:
        s = s[1:-1]
        if len(s) < 1:
            break
    
    print(len(s))