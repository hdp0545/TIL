def solution(board):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    N = len(board) # N은 보드 넓이
    answer = 500 * N ** 2 # 초기값은 이론상 최대치로
    for k in range(2): # 오른쪽으로 DFS 한번 아래방향으로 DFS 한번
        stack = [[0, 0, k]] #
        visit = [[[False, None]] * N for _ in range(N)]
        visit[0][0] = [0, k]
        while stack:
            y, x, d = stack.pop()
            if x == N-1 and y == N-1:
                answer = min(answer, visit[y][x][0])
            else:
                for i in range(3, -1, -1):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N:
                        if board[ny][nx] == 0:
                            if d == i:
                                if visit[ny][nx][0] == False or visit[y][x][0] + 100 < visit[ny][nx][0]:
                                    visit[ny][nx] = [visit[y][x][0] + 100, i]
                                    stack.append([ny, nx, i])
                            else:
                                if visit[ny][nx][0] == False or visit[y][x][0] + 600 < visit[ny][nx][0]:
                                    visit[ny][nx] = [visit[y][x][0] + 600, i]
                                    stack.append([ny, nx, i])
    return answer

print(solution([[0,0,0],[1,0,1],[0,0,0]]))