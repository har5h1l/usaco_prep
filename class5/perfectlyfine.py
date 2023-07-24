# https://codeforces.com/contest/1829/problem/C

for _ in range(int(input())):

    t1, i1, i2 = 400001, 200001, 200001
    a, b, c = False, False, False

    for i in range(int(input())):
        m, s = input().split()

        if s == '11':
            t1 = min(t1, int(m))
            a = True
        elif s == '01':
            i1 = min(i1, int(m))
            b = True
        elif s == '10':
            i2 = min(i2, int(m))
            c = True

    if a: print(min(i1+i2, t1))
    elif b == True and c == True: print(min(i1+i2, t1))
    else: print(-1)