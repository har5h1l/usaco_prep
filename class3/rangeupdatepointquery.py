# https://codeforces.com/contest/1791/problem/F

for _ in range(int(input())):
    n, q = list(map(int, input().split()))
    a = input().split()

    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            l, r = int(query[1]), int(query[2])
            for i in range(l-1, r):
                a[i] = str(sum([int(j) for j in a[i]]))
        else:
            print(a[int(query[1])-1])