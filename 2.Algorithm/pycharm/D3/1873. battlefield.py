def control(command):
    if command == 'U':
        return 0
    if command == 'D':
        return 1
    if command == 'L':
        return 2
    if command == 'R':
        return 3
    if command == 'S':
        return 4


for test_case in range(1, int(input())+1):
#탱크의 상태
    tank_mode = ['^', 'v', '<', '>']
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
#탱크맵 다운
    H, W = (map(int, input().split()))
    matrix = [[0]*W for _ in range(H)]
    for j in range(H):
        for i, a in enumerate(input()):
            matrix[j][i] = a
            if a in tank_mode:
                tank_i, tank_j = i, j
                tank_stat = a

#탱크 이동
    N = int(input())
    command = input()
    for c in command:
        idx = control(c)
        if idx == 4:
            s_idx = tank_mode.index(tank_stat)
            s_i, s_j = tank_i + dx[s_idx], tank_j + dy[s_idx]
            while 0 <= s_i < W and 0 <= s_j < H:
                if matrix[s_j][s_i] == '#':
                    break
                if matrix[s_j][s_i] == '*':
                    matrix[s_j][s_i] = '.'
                    break
                s_i += dx[s_idx]
                s_j += dy[s_idx]
        else:
            if 0 <= tank_j+dy[idx] < H and 0 <= tank_i+dx[idx] < W:
                if matrix[tank_j+dy[idx]][tank_i+dx[idx]] == '.':
                    matrix[tank_j+dy[idx]][tank_i+dx[idx]] = tank_mode[idx]
                    matrix[tank_j][tank_i] = '.'
                    tank_j, tank_i = tank_j+dy[idx], tank_i+dx[idx]
                    tank_stat = tank_mode[idx]
                else:
                    matrix[tank_j][tank_i] = tank_stat = tank_mode[idx]
            else:
                matrix[tank_j][tank_i] = tank_stat = tank_mode[idx]

    print('#{}'.format(test_case),end=' ')
    for m in matrix:
        print(''.join(m))




        
    

            