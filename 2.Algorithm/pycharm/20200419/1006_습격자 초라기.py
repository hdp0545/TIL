dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

T = int(input())
for tc in range(1, T+1):
    N, W = map(int, input().split())
    circle = [list(map(int, input().split())), list(map(int, input().split()))]
    visit = [[0]*N for _ in range(2)]
    for i in range(2):
        for j in range(N):
            stack = [(i,j)]
            while stack:
                r, c = stack.pop()
                visit[r][c] = 1
                for d in range(4):
                    ni, nj = i + dy[d], j + dx[d]
                    if 0 <= ni < 2:
                        if not 0 <= nj < N:
                            nj %= N
                        if circle[i][j] + circle[ni][nj] <= W and visit[ni][nj]:
                            stack += [(ni, nj)]
                if len(stack) == 1:
                    


            data[i][j] = stack
    print(data)