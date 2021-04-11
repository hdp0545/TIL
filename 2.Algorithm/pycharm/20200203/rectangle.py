import pprint

for test_case in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = []
    T = [[0]*10 for _ in range(10)]
    cnt = 0
    for x in range(N):
        for i in range(10):
            for j in range(10):
                if matrix[x][0] <= i and i <= matrix[x][2] and matrix[x][1] <= j and j <= matrix[x][3]:
                    if T[i][j] == 0:
                        cnt -= 1
                    if T[i][j] != matrix[x][4]:
                        cnt += 1
                        T[i][j] = matrix[x][4]


    print('#{} {}'.format(test_case, cnt))

