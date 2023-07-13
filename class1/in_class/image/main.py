# https://codeforces.com/problemset/problem/1721/A

for _ in range(int(input())):
    print(len(set(input() + input())) - 1)