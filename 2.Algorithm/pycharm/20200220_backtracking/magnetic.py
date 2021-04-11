for test_case in range(1, 11):
    input()
    matrix = [list(map(int, input().split())) for _ in range(100)]
    result = 0
    for j in range(100):
        flag = 0
        for i in range(100):
            if flag == 0:
                if matrix[i][j] == 1:
                    flag = 1
            else:
                if matrix[i][j] == 2:
                    result += 1
                    flag = 0
    print('#{} {}'.format(test_case, result))