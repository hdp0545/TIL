from queue import PriorityQueue as pq

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

for tc in range(1, int(input())+1):
    N = int(input())
    map = [[int(n) for n in input()] for _ in range(N)]
    djikstra = [[90000] * N for _ in range(N)]
    que = pq()
    que.put((0, 0, 0))
    djikstra[0][0] = 0
    while que:
        d, r, c = que.get()
        if d > djikstra[N-1][N-1]:
            break
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                nd = d + map[nr][nc]
                if djikstra[nr][nc] > nd:
                    djikstra[nr][nc] = nd
                    que.put((nd, nr, nc))
    print(f'#{tc} {djikstra[N-1][N-1]}')
