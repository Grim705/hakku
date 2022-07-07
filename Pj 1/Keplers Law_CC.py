T = int(input())
for i in range(0, T):
    a, b, c, d = map(int, input().split())
    if 1 <= a <= 10 and 1 <= b <= 10 and 1 <= c <= 10 and 1 <= d <= 10:
        if pow(a, 2)/pow(c, 3) == pow(b, 2)/pow(d, 3):
            print("Yes")
        else:
            print("No")
