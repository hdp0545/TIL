def f():
    for i in range(N - R + 1):
        for j in range(M - C + 1):
            if match(i, j):
                stick(i, j)
                return True
    return False


def match(i, j):
    for r in range(R):
        for c in range(C):
            if sticker[r][c]:
                if note[i+r][j+c]:
                    return False
    return True


def stick(i, j):
    global cnt
    global note
    for r in range(R):
        for c in range(C):
            if sticker[r][c]:
                note[i+r][j+c] = 1
                cnt += 1


N, M, K = map(int, input().split())
note = [[0]*M for _ in range(N)]
cnt = 0
for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]
    for _ in range(4):
        if f():
            break
        sticker = [[sticker[i][j] for i in range(R-1, -1, -1)] for j in range(C)]
        R, C = C, R
print(cnt)