# https://codeforces.com/problemset/problem/1788/A

ans = [] # contains all the values of k
t = int(input()) # number of test cases

for i in range(t):
    # inputs for this case
    n = int(input())
    a = [int(i) for i in input().split()]

    # finding k
    k = -1
    for i in range(1, n):
        left = a[:i].count(2)
        right = a[i:].count(2)
        if left == right:
            k = i
            break
    ans.append(k)

# printing all the values of k
for k in ans:
    print(k)