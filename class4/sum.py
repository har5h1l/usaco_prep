# https://codeforces.com/contest/1742/problem/A 

for _ in range(int(input())):
    a, b, c = list(map(int, input().split()))
    print('YES' if a + b == c or a + c == b or b + c == a else 'NO')