# http://www.usaco.org/index.php?page=viewproblem2&cpid=1084

n = int(input())
ids = list(map(lambda x: int(x) % 2, input().split()))

e = ids.count(0)
o = n - e

while o > e:
    o = o-2
    e += 1

if e > o+1: print(2*o + 1)
else: print(e + o)