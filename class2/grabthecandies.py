# https://codeforces.com/contest/1807/problem/B

for _ in range(int(input())):
    n = int(input())
    bags = list(map(int, input().split()))

    odd_sum = sum([i for i in bags if i % 2])
    even_sum = sum(bags) - odd_sum

    if even_sum > odd_sum:
        print('YES')
        
    else:
        print('NO')