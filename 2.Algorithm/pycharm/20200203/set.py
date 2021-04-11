for test_case in range(1, int(input())+1):
    N, K = (map(int, input().split()))
    N_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    result_matrix = []
    for i in range(1 << 12):
        sample = []
        for j in range(12):
            if i & (1 << j):
                sample.append(N_list[j])
        result_matrix.append([len(sample), sum(sample)])

    print('#{} {}'.format(test_case, result_matrix.count([N, K])))