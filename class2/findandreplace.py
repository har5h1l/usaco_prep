# https://codeforces.com/contest/1807/problem/C

for _ in range(int(input())):
    n = int(input())
    s = input()
    
    s_1 = set([s[i] for i in range(0, n, 2)])
    s_2 = set([s[i] for i in range(1, n, 2)])

    if len(s_1.intersection(s_2)) == 0:
        print('YES')
    else:
        print('NO')