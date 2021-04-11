def test(matrix, N):
    c = 0
    for i in range(8):
        for j in range(8 - N + 1):
            for n in range(N//2):
                if matrix[i][j + n] != matrix[i][j + N - 1 - n]:
                    break
            else:
                c += 1
    return c


for test_case in range(1, 11):
    N = int(input())
    matrix = [[w for w in input()] for _ in range(8)]
    cnt = test(matrix, N)
    new = list(map(list, zip(*matrix)))
    cnt += test(new, N)
    print('#{} {}'.format(test_case, cnt))