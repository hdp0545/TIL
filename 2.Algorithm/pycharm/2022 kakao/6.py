def solution(board, skill):
    N = len(board)
    M = len(board[0])
    answer = N * M
    for sk in skill:
        attack, r1, c1, r2, c2, degree = sk
        if attack == 1:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    bf = board[i][j]
                    board[i][j] -= degree
                    if bf > 0 and board[i][j] <= 0:
                        answer -= 1
        else:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    bf = board[i][j]
                    board[i][j] += degree
                    if bf <= 0 and board[i][j] > 0:
                        answer += 1
    return answer

print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))