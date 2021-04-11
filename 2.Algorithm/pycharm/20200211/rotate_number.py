for test_case in range(1, int(input())+1):
    print('#{}'.format(test_case))
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        l1 = [str(matrix[N-1-j][i]) for j in range(N)]
        l2 = [str(matrix[N-1-i][N-1-j]) for j in range(N)]
        l3 = [str(matrix[j][N-1-i]) for j in range(N)]
        print(''.join(l1), ''.join(l2), ''.join(l3), sep = ' ')