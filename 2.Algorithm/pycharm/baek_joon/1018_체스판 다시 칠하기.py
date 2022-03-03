N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
answers = []
for i in range(N-7):
    for j in range(M-7):
        cnt = 0
        for ni in range(i, i+8):
            for nj in range(j, j+8):
                if (ni + nj) % 2:
                    if board[ni][nj] == "W":
                        cnt += 1
                else:
                    if board[ni][nj] == "B":
                        cnt += 1
        if cnt > 32:
            cnt = 64 - cnt
        answers.append(cnt)
print(min(answers))