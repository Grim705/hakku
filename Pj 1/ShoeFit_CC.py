tc = int(input())
for i in range(0, tc):
    lst = list(map(int, input().split()[:3]))
    if all(ele == 0 for ele in lst) or all(ele == 1 for ele in lst):
        print(0)
    else:
        print(1)
