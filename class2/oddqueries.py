# 

for _ in range(int(input())):
    
    n, q = list(map(int, input().split()))
    a = [0] + list(map(lambda i: int(i) % 2, input().split()))
 
    for i in range(2, n+1):
        a[i] += a[i-1]

    s = a[-1]
 
    for _ in range(q):
 
        l, r, k = list(map(int, input().split()))
 
        k_sum = (r - l + 1) * k
        new_sum = s - a[r] + a[l - 1] + k_sum
 
        if new_sum % 2:
            print('YES')
 
        else:
            print('NO')