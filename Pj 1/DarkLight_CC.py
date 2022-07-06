T = int(input())
for i in range(0, T):
    x, y = map(int, input().split())
    if x % 4 != 0 and y == 0:
        print("On")
    elif x % 4 == 0 and y == 0:
        print("Off")
    elif x == 0 and y == 1:
        print("On")
    elif x % 4 == 0 and y == 1:
        print("On")
    else:
        print("Ambiguous")
