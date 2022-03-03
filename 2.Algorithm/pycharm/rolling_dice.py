def rolling(dice_raw, dice_column, command):
    if command == 1:
        temp = dice_raw[3]
        for i in range(2, -1, -1):
            dice_raw[i+1] = dice_raw[i]
        dice_raw[0] = temp
        dice_column[1] = dice_raw[1]
        dice_column[3] = dice_raw[3]

    if command == 2:
        temp = dice_raw[0]
        for i in range(3):
            dice_raw[i] = dice_raw[i+1]
        dice_raw[3] = temp
        dice_column[1] = dice_raw[1]
        dice_column[3] = dice_raw[3]

    if command == 3:
        temp = dice_column[0]
        for i in range(3):
            dice_column[i] = dice_column[i+1]
        dice_column[3] = temp
        dice_raw[1] = dice_column[1]
        dice_raw[3] = dice_column[3]

    if command == 4:
        temp = dice_column[3]
        for i in range(2, -1, -1):
            dice_column[i+1] = dice_column[i]
        dice_column[0] = temp
        dice_raw[1] = dice_column[1]
        dice_raw[3] = dice_column[3]


N, M, x, y, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))
dice_raw = [0] * 4
dice_column = [0] * 4
dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]
result = []
for command in commands:
    x += dx[command]
    y += dy[command]
    if 0 <= y < N and 0 <= x < M:
        rolling(dice_raw, dice_column, command)
        if matrix[y][x] == 0:
            matrix[y][x] = dice_raw[3]
        else:
            dice_raw[3] = matrix[y][x]
            dice_column[3] = matrix[y][x]
            matrix[y][x] = 0
        result.append(dice_raw[1])
    else:
        x -= dx[command]
        y -= dy[command]

print('\n'.join(map(str, result)))

