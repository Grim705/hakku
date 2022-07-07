T = int(input())
for i in range(0, T):
    race = int(input())
    lstA = list(map(int, input().split()[:race]))
    lstB = list(map(int, input().split()[:race]))
    A = sum(lstA) - max(lstA)
    B = sum(lstB) - max(lstB)
    if A < B:
        print("Alice")
    elif B < A:
        print("Bob")
    else:
        print("Draw")
