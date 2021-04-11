dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

T = int(input())
for tc in range(1, T+1):
    sky =[[0]*12] + [[0] + list(map(int, input().split())) + [0] for _ in range(10)] + [[0]*12]
    cnt = 0
    for i in range(1, 11):
        for j in range(1, 11):
            if sky[i][j]:
                sky[i][j] = 0
                cnt += 1
                st = [(i, j)]
                while st:
                    i, j = st.pop()
                    for k in range(8):
                        ni, nj = i+dy[k], j+dx[k]
                        if sky[ni][nj]:
                            st += [(ni, nj)]
                            sky[ni][nj] = 0
    print(f'#{tc} {cnt}')