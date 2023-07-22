# https://codeforces.com/contest/1829/problem/A

for _ in range(int(input())): 
    s = input()
    print(len([i for i in range(len(s)) if s[i] != 'codeforces'[i]]))