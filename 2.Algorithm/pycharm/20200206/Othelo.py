for test_case in range(1, int(input())+1):
    N, M = (map(int, input().split()))
    # 초기 배열
    matrix = [[0]*(N+2) for _ in range(N+2)]
    matrix[N//2 + 1][N//2 + 1] = matrix[N//2][N//2] = 2
    matrix[N//2][N//2 + 1] = matrix[N//2 + 1][N//2] = 1

    #컨트롤 인풋1
    dx = [0, 0, 1, -1, 1, -1, 1, -1]
    dy = [1, -1, 0, 0, 1, -1, -1, 1]
    for _ in range(M):
        x, y, color = map(int, input().split())
        matrix[y][x] = color
        for i in range(8):
            new_x = x + dx[i]
            new_y = y + dy[i]
            cnt = 0
            while matrix[new_y][new_x] != 0:
                if matrix[new_y][new_x] == color:
                    for n in range(1, cnt+1):
                        matrix[y + n*dy[i]][x + n*dx[i]] = color
                    break
                new_x += dx[i]
                new_y += dy[i]
                cnt += 1

    #개수세기
    result_1 = 0
    result_2 = 0
    for c in range(1, N+1):
        result_1 += matrix[c].count(1)
        result_2 += matrix[c].count(2)
    print('#{} {} {}'.format(test_case, result_1, result_2))

