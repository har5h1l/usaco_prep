# https://codeforces.com/problemset/problem/1772/B

beautiful = lambda m: (m, [m[0], m[2], m[1], m[3]])
for _ in range(int(input())):
    m = list(map(int, input().split() + input().split()))
    b = beautiful(sorted(m))

    if (m in b) or ([m[2], m[0], m[3], m[1]] in b) or (m[::-1] in b) or ([m[1], m[3], m[0], m[2]] in b):
        print('YES')
    else:
        print('NO')