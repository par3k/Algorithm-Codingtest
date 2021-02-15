T = int(input())
cmd = input().split()

x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in cmd:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            move_x = x + dx[i]
            move_y = y + dy[i]

    if move_x < 1 or move_y < 1 or move_x > T or move_y > T:
        continue
    x, y = move_x, move_y

print(x, y)