from _collections import deque

direct = [(0, -1), (-1, 0), (0, 1)]


def bfs(y, x, d):
    deq = deque()
    visited = [[0]*M for _ in range(N)]
    s = []
    deq.append((y, x, d))
    if matrix[y][x] and (y, x) not in kill_list:
        kill_list.append((y, x))
        return
    visited[y][x] = 1
    flag = False
    while deq:
        here = deq.popleft()
        y, x, d = here
        if flag:
            min_y, min_x = s[0][0], s[0][1]
            for idx in range(1, len(s)):
                if s[idx][1] < min_x:
                    min_y, min_x = s[idx][0], s[idx][1]
            if (min_y, min_x) not in kill_list:
                kill_list.append((min_y, min_x))
            return

        for dir in range(len(direct)):
            new_y, new_x = y+direct[dir][0], x+direct[dir][1]
            if 0<=new_y<N and 0<=new_x<M and matrix[new_y][new_x] and not visited[new_y][new_x] and d+1 <= D:
                s.append((new_y, new_x))
                flag = True
            elif not s and 0 <= new_y < N and 0 <= new_x < M and not visited[new_y][new_x] and d+1<D:
                deq.append((new_y, new_x, d+1))
                visited[new_y][new_x] = 1
        if s and not deq:
            min_y, min_x = s[0][0],s[0][1]
            for idx in range(1, len(s)):
                if s[idx][1] < min_x:
                    min_y, min_x = s[idx][0], s[idx][1]
            if (min_y, min_x) not in kill_list:
                kill_list.append((min_y, min_x))
            return


N, M, D = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
matrix_temp = [[0]*M for _ in range(N)]
max_kill = 0
for i in range(N):
    for j in range(M):
        matrix_temp[i][j] = matrix[i][j]
for i in range(M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            # 카피
            for y in range(N):
                for x in range(M):
                    matrix[y][x] = matrix_temp[y][x]

            isExist = True
            kill = 0
            while isExist:
                isExist = False
                for y in range(N-1, -1, -1):
                    for x in range(M):
                        if matrix[y][x]:
                            isExist = True
                            break
                    if isExist:
                        break

                if not isExist: break
                kill_list = []
                bfs(N-1, i, 1)
                bfs(N-1, j, 1)
                bfs(N-1, k, 1)
                kill += len(kill_list)
                if kill_list:
                    for dead_man in kill_list:
                        #죽은 적의 죄표 값 0으로 바꿈
                        r, c = dead_man
                        matrix[r][c] = 0
                #적이동
                for y in range(N-2, -1, -1):
                    for x in range(M):
                        if matrix[y][x]:
                            matrix[y+1][x] = 1
                            matrix[y][x] = 0
                        else:
                            matrix[y+1][x] = 0

            #죽인 적이 최대인지 비교
            if kill > max_kill:
                max_kill = kill
print(max_kill)