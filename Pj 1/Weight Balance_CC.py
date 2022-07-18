T = int(input())
for i in range(0, T):
    flag = 1
    w1, w2, x1, x2, M = map(int, input().split())
    increase = w2-w1
    for x in range(x1*M, (x2*M)+1):
        if x == increase:
            print("1")
            flag = 1
            break
        else:
            flag = 0
            continue
    if flag == 0:
        print("0")
    else:
        pass
