from queue import PriorityQueue
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution(cars):
    N = len(cars)
    que = PriorityQueue()
    visit = [[False] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if cars[i][j] == 1:
                que.put((0, i, j))
                visit[i][j] = True
                flag = True
                break
        if flag:
            break

    while que:
        cnt, i, j = que.get()
        for k in range(4):
            ni = i + dy[k]
            nj = j + dx[k]
            if 0 <= ni < N and 0 <= nj < N:
                if not visit[ni][nj]:
                    if cars[ni][nj] == 2:
                        que.put((cnt+1, ni, nj))
                        visit[ni][nj] = True
                    elif cars[ni][nj] == 0:
                        que.put((cnt, ni, nj))
                        visit[ni][nj] = True
                    elif cars[ni][nj] == 4:
                        return cnt
    return -1

print(solution([[0,0,3,0,0,0,0], [1,0,3,0,0,0,0], [0,0,3,0,0,0,0], [0,0,2,0,0,3,3], [2,2,2,0,2,0,0],[3,3,2,0,2,0,3],[3,3,2,0,2,0,4]]))