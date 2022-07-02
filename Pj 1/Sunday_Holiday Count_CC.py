def holidays(date, counter):
    hdd = [6, 13, 20, 27, 7, 14, 21, 28]
    for info in date:
        if info not in hdd:
            counter = counter + 1
        else:
            continue
    return counter


n = int(input())
count = 8
for i in range(0, n):
    hd = int(input())
    lst = list(map(int, input().split()[:hd]))
    print(holidays(lst, count))
