from collections import deque as dq
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def move(r, c, d):
    color = matrix[r][c]
    matrix[r][c] = '.'
    r, c = r + dy[d], c + dx[d]
    while matrix[r][c] == '.' or matrix[r][c] == 'O':
        if matrix[r][c] == 'O':
            return False
        else:
            r, c = r + dy[d], c + dx[d]
    r, c = r-dy[d], c-dx[d]
    matrix[r][c] = color
    return r, c


def bfs(q):
    visit = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    for step in range(1, 11):
        temp = dq([])
        while q:
            (rr, rc), (br, bc) = q.popleft()
            visit[rr][rc][br][bc] = 1
            for d in range(4):
                matrix[rr][rc], matrix[br][bc] = 'R', 'B'
                blue_ball = move(br, bc, d)
                red_ball = move(rr, rc, d)
                if blue_ball:
                    nbr, nbc = blue_ball
                    blue_ball = move(nbr, nbc, d)
                    if blue_ball:
                        if red_ball:
                            nrr, nrc = red_ball
                            matrix[nrr][nrc] = '.'
                            nbr, nbc = blue_ball
                            matrix[nbr][nbc] = '.'
                            if visit[nrr][nrc][nbr][nbc] == 0:
                                visit[nrr][nrc][nbr][nbc] = 1
                                temp.append((red_ball, blue_ball))
                        else:
                            return step
                    else:
                        if red_ball:
                            nr, nc = red_ball
                            matrix[nr][nc] = '.'
                else:
                    if red_ball:
                        nr, nc = red_ball
                        matrix[nr][nc] = '.'
        q = temp
    return -1


N, M = map(int, input().split())
matrix = [[d for d in input()] for _ in range(N)]
for i in range(1, N-1):
    for j in range(1, M-1):
        if matrix[i][j] == 'R':
            red_ball = (i, j)
            matrix[i][j] = '.'
        elif matrix[i][j] == 'B':
            blue_ball = (i, j)
            matrix[i][j] = '.'
q = dq([(red_ball, blue_ball)])
result = bfs(q)
print(result)