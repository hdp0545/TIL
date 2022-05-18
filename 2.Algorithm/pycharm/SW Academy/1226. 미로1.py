dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(10):
    case = input()
    matrix = [list(input()) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if matrix[i][j] == '2':
                sp = (i, j)
                break
    answer = '0'
    stack = [sp]
    while stack:
        i, j = stack.pop()
        for d in range(4):
            ni, nj = i + dy[d], j + dx[d]
            if matrix[ni][nj] == '0':
                stack.append((ni, nj))
                matrix[ni][nj] = '1'
            elif matrix[ni][nj] == '3':
                answer = '1'
                break
    print('#' + case + ' ' + answer)