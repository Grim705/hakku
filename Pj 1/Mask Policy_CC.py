T = int(input())
for i in range(0, T):
    x, y = map(int, input().split())
    if (x-y) < y:
        print(x-y)
    elif (x-y) > y:
        print(y)
    else:
        print(y)
