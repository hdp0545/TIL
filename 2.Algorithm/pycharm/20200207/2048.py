dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def delete_zero(matrix, c):
    r = c % 2
    a = c // 2

    for i in range(N):
        if a:
            ni = (N - 1) * r
            nj = (N - 1) * r + ((-2 * r) + 1) * i
        else:
            ni = (N - 1) * r + ((-2 * r) + 1) * i
            nj = (N - 1) * r

        cnt = 0
        
        while 0 <= nj - cnt*dy[c] < N and 0 <= ni - cnt*dx[c] < N:
            if matrix[nj - cnt*dy[c]][ni - cnt*dx[c]] == 0 :
                cnt += 1
            else:
                matrix[nj][ni] = matrix[nj - cnt*dy[c]][ni - cnt*dx[c]]
                nj -= dy[c]
                ni -= dx[c]
        for cnt_i in range(cnt):
            matrix[nj - cnt_i*dy[c]][ni - cnt_i*dx[c]] = 0

    return matrix


for test_case in range(1, int(input())+1):
    N, S = input().split()
    N = int(N)
    matrix = [list(map(int, input().split())) for i in range(int(N))]

    command = ['up', 'down', 'left', 'right']
    c = command.index(S)

    r = c % 2
    a = c // 2

    matrix = delete_zero(matrix, c)

    for j in range(1, N):
        for i in range(N):  # type: int
            if a:
                ni = (N - 1) * r + ((-2 * r) + 1) * j
                nj = (N - 1) * r + ((-2 * r) + 1) * i
            else:
                ni = (N - 1) * r + ((-2 * r) + 1) * i
                nj = (N - 1) * r + ((-2 * r) + 1) * j
           
            if matrix[nj][ni] == matrix[nj + dy[c]][ni + dx[c]]:
                matrix[nj + dy[c]][ni + dx[c]] = matrix[nj + dy[c]][ni + dx[c]] * 2
                matrix[nj][ni] = 0

    matrix = delete_zero(matrix, c)

    print('#{}'.format(test_case))
    for _ in range(N):
        print(' '.join(map(str, matrix[_])))