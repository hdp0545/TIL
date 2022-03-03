for test_case in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int, [n for n in input()])) for _ in range(N)]
    result = 0
    c = N // 2
    for i in range(N):
        di = (N//2) - abs(i - (N//2))
        result += sum(matrix[i][c-di:c+di+1])
    print('#{} {}'.format(test_case, result))