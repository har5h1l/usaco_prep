# https://codeforces.com/contest/1742/problem/E

for _ in range(int(input())):
    
    # inputs
    n, q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    K = list(map(int, input().split()))

    # prefix
    steps = a[:]
    s = steps[0]
    for i in range(1, n):
        s += steps[i]
        steps[i] = s

    # max_prefix
    heights = a[:]
    m = heights[0]
    for i in range(1, n):
        if heights[i] >= m: m = heights[i]
        else: heights[i] = m

    # binary search
    out = []
    for k in K:
        if k != 0:
            l, r, i = 0, n-1, None
            while l < r:
                if i != int((l+r)/2): i = int((l+r) / 2)
                else:
                    if heights[l] <= k and heights[r] <= k: i = r
                    break
                if heights[i] <= k: l = i
                else: r = i
            out.append(str(steps[i]))
        else: out.append('0')
    
    print(' '.join(out))