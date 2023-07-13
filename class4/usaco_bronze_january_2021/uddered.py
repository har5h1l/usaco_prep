# http://www.usaco.org/index.php?page=jan21results

c, h = input(), input()
print(1 + len([i for i in range(len(h)-1) if c.index(h[i]) >= c.index(h[i+1])]))