# http://www.usaco.org/index.php?page=viewproblem2&cpid=1085

def count(c):
    out = 0
    for i in b:
        if c <= i: out += 1
        else: return out
    return out

n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
b = sorted(list(map(int, input().split())), reverse=True)

i = 0
ans = 1
for c in a:
    ans *= count(c) - i
    i += 1

print(ans)