for test_case in range(1, int(input())+1):
    N = int(input())
    maze = [[1]*(N+2) for _ in range(N+2)]
    for i in range(N):
        temp = list(map(int, input()))
        for j in range(N):
            maze[i+1][j+1] = temp[j]
            if temp[j] == 2:
                si, sj, d = i+1, j+1, 0
        del temp
    stack = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    stack.append((si, sj, d))
    result = 0
    while stack:
        if maze[si][sj] != 1:
            if maze[si][sj] == 3:
                result = 1
                break
            maze[si][sj] = 1
        for i in range(4):
            if maze[si+dy[i]][sj+dx[i]] != 1 and i != d:
                stack.append((si+dy[i], sj+dx[i], i))
        if maze[si+dy[d]][sj+dx[d]] != 1:
            si, sj = si + dy[d], sj + dx[d]
        else:
            si, sj, d = stack.pop(-1)
    print('#{} {}'.format(test_case, result))