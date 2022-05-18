pipe = [[False, False, False, False],
        [True, True, True, True],
        [True, False, False, True],
        [False, True, True, False],
        [True, False, True, False],
        [False, False, True, True],
        [False, True, False, True],
        [True, True, False, False]]

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

for t in range(1, int(input())+1):
    N, M, R, C, L = map(int, input().split())
    arr = [[0] * (M+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M+2)]
    st = []
    cnt = 0
    st.append((R+1, C+1, L))
    while st:
        R, C, L = st.pop()
        if L:
            for k in range(4):
                if pipe[arr[R][C]][k] and pipe[arr[R + dy[k]][C + dx[k]]][-k-1]:
                    st.append((R + dy[k], C + dx[k], L-1))
            cnt += 1
            arr[R][C] = 0
    print('#{} {}'.format(t, cnt))