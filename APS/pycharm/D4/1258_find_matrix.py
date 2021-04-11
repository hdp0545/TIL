def my_lambda(x):
    return x[0]

for test_case in range(1, int(input()) + 1):
    N = int(input())
    matrix =[[0] * (N+2)]
    matrix.extend([[0] + list(map(int, input().split())) + [0] for _ in range(N)])
    matrix.append([0]*(N+2))
    result_list = []
    for i in range(1, N):
        for j in range(1, N):
            if matrix[i][j]:
                si, sj = i, j
                ei, ej = i, j
                while matrix[ei][ej]:
                    ei += 1
                ei -= 1
                while matrix[ei][ej]:
                    ej += 1
                ej -= 1
                result_list.append([ei - si + 1, ej - sj + 1])
                for di in range(si, ei + 1):
                    for dj in range(sj, ej + 1):
                        matrix[di][dj] = 0
    result_list.sort(key=lambda x: x[0])

    result_list.sort(key=lambda x: x[0]*x[1])
    results = []
    for r in result_list:
        results.extend(map(str, r))
    print('#{} {} {}'.format(test_case, len(result_list), ' '.join(results)))