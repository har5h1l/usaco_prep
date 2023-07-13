# https://codeforces.com/contest/1807/problem/E

def ask():
    print('?', ' '.join(j))
    return int(input())

for _ in range(int(input())):
    n = int(input())
    a = input().split()

    k = int(n/2)
    i = 0

    while True:
        j = a[i : k+1]
        x = ask()

        if sum(list(map(int, j))) == x:
            i = k
            k *= 2
        
        elif len(j) == 1:
            print('!', j[0])
            break

        else:
            k /= 2

        x = ask()