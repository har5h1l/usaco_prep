# usaco.org/index.php?page=viewproblem2&cpid=1060

n = int(input())
nums = list(map(int, input().split()))

out = 0

for i in range(n):
    for j in range(i, n):
        x = nums[i:j+1]
        if x.count(sum(x)/len(x)) > 0:
            out += 1
            
print(out)