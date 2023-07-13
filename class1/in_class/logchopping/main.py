for _ in range(int(input())):
    n = int(input())
    actions = sum(map(int, input().split())) - n
    if actions % 2: # sum % 2 == 1
        print('errorgorn')
    else:
        print('maomao90')