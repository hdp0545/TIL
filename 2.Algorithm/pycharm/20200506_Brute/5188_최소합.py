dy = [1, 0]
dx = [0, 1]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    stack = [(0, 0, arr[0][0])]
    min_sum = 250
    while stack:
        r, c, s = stack.pop()
        if r == N-1 and c == N-1 and s < min_sum:
            min_sum = s
        for d in range(2):
            nr, nc = r+dy[d], c+dx[d]
            if 0 <= nr < N and 0 <= nc < N and s < min_sum:
                stack.append((nr, nc, s + arr[nr][nc]))
    print(f'#{tc} {min_sum}')
