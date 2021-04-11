for test_case in range(1):
    N = int(input())
    matrix = [[w for w in input()] for _ in range(8)]
    cnt = 0
    for _ in range(2):
        for j in range(8):
            for i in range(8-N+1):
                print(matrix[j][i:i+N], matrix[j][i+N-1::-1][:N])
                if matrix[j][i:i+N] == matrix[j][i+N-1::-1][:N]:
                    cnt += 1
        matrix = list(map(list, zip(*matrix)))
    print('#{} {}'.format(test_case, cnt))