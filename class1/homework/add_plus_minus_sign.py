# https://codeforces.com/problemset/problem/1774/A

for _ in range(int(input())):
    value = input() # n
    a = input()

    value = bool(int(a[0]))

    for i in a[1:]:
        if i == '0':
            print('+', end='')

        else:
            if value: # is True (1)
                print('-', end='')
                value = False

            else: # value = False (0)
                print('+', end='')
                value = True

    print()