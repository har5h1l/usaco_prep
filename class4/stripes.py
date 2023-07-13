# https://codeforces.com/contest/1742/problem/C

for _ in range(int(input())):
    out = 'B'
    for _ in range(9):
        if input() == 'RRRRRRRR': 
            out = 'R'
    print(out)