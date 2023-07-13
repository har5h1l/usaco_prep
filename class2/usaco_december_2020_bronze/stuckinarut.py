n = int(input())

north = []
east = []

i = 0
for _ in range(n):

    z = input()

    if x[0] == 'N':
        north.append(z.split()[1::-1], i)

    else:
        east.append(z.split()[1:])
    
    i += 1

sorted_east = sorted(east, reverse=True)
sorted_north = sorted(north, reverse=True)

out = []

for z in sorted_north[1:]:
    y, x, i = z
    out.append(i, )

for i in range(n):
    if i == 0:
        out.append(sorted_north[0][-1], 'infinity')
    z = sorted_north[i]
    y, x, i = z
