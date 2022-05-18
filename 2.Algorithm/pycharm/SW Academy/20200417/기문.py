dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def is_wall(x, y):
    if 0 <= x < 10 and 0<= y < 10:
        return True
    return False



T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(10) ]
    v = [[0]*10 for _ in range(10)]
    #좌부터 시계방향
    count = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 1:
                if v[i][j] == 0:
                    stack = [[i, j]]
                    count += 1
                    while stack:
                        for n in range(8):
                            if is_wall(stack[0][0] + dx[n], stack[0][1] + dy[n]):
                                if arr[stack[0][0] + dx[n]][stack[0][1] + dy[n]] == 1:
                                    if v[stack[0][0] + dx[n]][stack[0][1] + dy[n]] != 1:
                                        v[stack[0][0] + dx[n]][stack[0][1] + dy[n]] = 1
                                        stack.append([stack[0][0] + dx[n], stack[0][1] + dy[n]])
                        stack.pop(0)

    print('#{} {}'.format(tc, count))