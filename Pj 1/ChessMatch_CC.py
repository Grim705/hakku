tc = int(input())
for i in range(0, tc):
    x, y, z = map(int, input().split())
    val = (180+x)*2
    total_time = y+z
    game_time = val - total_time
    print(game_time)