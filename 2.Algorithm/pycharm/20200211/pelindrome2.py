def my_pelindrome(matrix):
    N = 100
    while True:
        N -= 1
        for j in range(100):
            for i in range(100 - N + 1):
                for n in range(N//2):
                    if matrix[j][i + n] != matrix[j][i + N - 1 - n]:
                        break
                else:
                    return N


for _ in range(10):
    test_case = input()
    matrix = [[w for w in input()] for _ in range(100)]
    r1 = my_pelindrome(matrix)
    matrix = list(map(list, zip(*matrix)))
    r2 = my_pelindrome(matrix)
    print('#{} {}'.format(test_case, max(r1, r2)))