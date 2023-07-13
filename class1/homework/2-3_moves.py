# https://codeforces.com/problemset/problem/1716/A

for _ in range(int(input())):
    n = int(input())
    if n % 3 == 0:
        print(int(n/3))
    elif n != 1:
        if n % 3 == 2:
            print(int((n-2)/3 + 1))
        else:
            print(int((n-4)/3 + 2))
    else:
        print(2)