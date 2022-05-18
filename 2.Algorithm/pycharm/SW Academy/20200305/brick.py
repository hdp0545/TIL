di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
def remove(c, N, W, H, br):
    q = []
    r = 0
    while r < H and br[r][c] == 0:
        r += 1
    if r == H:
        return
    q.append((r, c))
    while q:
        i, j = q.pop()
        k = br[i][j]
        br[i][j] = 0
        for dis in range(1, k):
            for dir in range(4):
                ni = i + dis*di[dir]
                nj = j + dis*dj[dir]
                if 0 <= ni < H and 0 <= nj < W:
                    q.append((ni,nj))


def shoot(N, W, H):
    br = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            br[i][j] = org[i][j]
    for i in range(N):
        remove(p[i], N, W, H, br)
        for i in range(W):
            st = []
            for j in range(H-1, -1, -1):
                if br[j][i]:
                    st.append(br[j][i])
                    br[j][i] = 0
            for j in range(0, len(st)):
                br[H-1-j][i] = st[j]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if br[i][j]:
                cnt += 1
    return cnt


def npr(n, k, W, H):
    global minV
    if n == k:
        r = shoot(k, W, H)
        if minV > r:
            minV = r
    else:
        for i in range(W):
            p[n] = i
            npr(n+1, k, W, H)
            if minV == 0:
                return


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    org = [list(map(int, input().split())) for _ in range(H)]
    p = [0] * N
    minV = 100000000
    npr(0, N, W, H)
    print('#{} {}'.format(tc, minV))