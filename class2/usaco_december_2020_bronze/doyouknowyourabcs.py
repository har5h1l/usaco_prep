# http://www.usaco.org/index.php?page=viewproblem2&cpid=1059

nums = sorted(list(map(int, input().split())))
a, b = nums[0], nums[1]
c = nums[-1] - a - b
print(a, b, c)

# print((nums:=sorted(list(map(int, input().split()))))[0], nums[1], nums[-1] - nums[0] - nums[1])