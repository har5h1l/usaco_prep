# https://codeforces.com/contest/1791/problem/B

for _ in range(int(input())):
    n = input()
    
    x, y = 0, 0
    out = 'NO'

    for m in input():
    
        if m == 'U': y += 1
        elif m == 'D': y -= 1
        elif m == 'R': x += 1
        else: x -= 1
        
        if x == 1 and y == 1:
            out = 'YES'
            break

    print(out)