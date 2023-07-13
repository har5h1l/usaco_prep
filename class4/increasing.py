# https://codeforces.com/contest/1742/problem/B

for _ in range(int(input())):
    _ = input()
    a = input().split()
    print('YES' if len(set(a)) == len(a) else 'NO')