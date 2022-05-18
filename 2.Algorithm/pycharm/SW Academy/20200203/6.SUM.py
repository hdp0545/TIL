
for test_case in range(1, 11):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    results = []
    j_sum = 0
    for raw in matrix:
        results.append(sum(raw))
    for i in range(100):
        for j in range(100):

            j_sum += matrix[j][i]

        results.append(j_sum)
        j_sum = 0

    for i in range(100):
        j_sum += matrix[i][i]
    results.append(j_sum)
    j_sum = 0

    for i in range(100):
        j_sum += matrix[i][99 - i]
    results.append(j_sum)

    print('#{} {}'.format(test_case, max(results)))
