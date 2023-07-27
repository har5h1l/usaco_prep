# https://codeforces.com/contest/1811/problem/A

for _ in range(int(input())):
    n, d = list(map(int, input().split()))
    s = input().split() + ['-1']

    for i in range(n+1): 
        print(i, s[i])
        if int(s[i]) <= d: 
            s.insert(i, str(d))
            break
        
    print(''.join(s[:len(s) - 1]))