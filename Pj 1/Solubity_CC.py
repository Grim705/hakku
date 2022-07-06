tc = int(input())
for i in range(0, tc):
    lst = list(map(int, input().split()[:3]))
    if 31 <= lst[0] <= 40 and 101 <= lst[1] <= 120 and 1 <= lst[2] <= 5:
        val = lst[1]+(100-lst[0])*lst[2]
        val = val * 10
        print(val)
    else:
        continue
