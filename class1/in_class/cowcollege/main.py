# http://usaco.org/index.php?page=viewproblem2&cpid=125

# inputs
n = int(input())
c = list(map(int, input().split()))
c.sort()

# answer variables
best_m = 0
best_f = 0

# solve
for f in c:
    m = 0
    for max_f in c:
        if f <= max_f:
            m += f
    
    if m > best_m:
        best_m = m
        best_f = f

# answer
print(best_m, best_f)