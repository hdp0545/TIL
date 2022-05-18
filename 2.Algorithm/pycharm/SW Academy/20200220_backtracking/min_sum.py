def backtrack(mat, N, check, k=0, r=0):
    c = []
    global min1
    if r > min1:
        return
    if k == N:
        if r < min1:
            min1 = r
    else:
        for i in range(N):
            if check[i]:
                c.append(i)
        for i in range(N-k):
            check[c[i]] = False
            backtrack(mat, N, check, k+1, r + mat[k][c[i]])
            check[c[i]] = True


for test_case in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    check = [True] * N
    min1 = 1001
    backtrack(matrix, N, check)
    print('#{} {}'.format(test_case, min1))