dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def f(i, j, st, k=1):
    if k == 7:
        result.add(st)
        return
    else:
        for l in range(4):
            if 0 <= i+dy[l] < 4 and 0 <= j+dx[l] < 4:
                f(i+dy[l], j+dx[l], st + arr[i+dy[l]][j+dx[l]], k+1)


for tc in range(1, int(input())+1):
    arr = [list(input().split()) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            f(i, j, arr[i][j])
    print('#{} {}'.format(tc, len(result)))
