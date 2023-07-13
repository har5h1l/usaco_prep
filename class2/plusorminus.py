# https://codeforces.com/contest/1807/problem/A

[print("+") if sum((s := list(map(int, input().split())))[:2]) == s[2] else print("-") for _ in range(int(input()))]