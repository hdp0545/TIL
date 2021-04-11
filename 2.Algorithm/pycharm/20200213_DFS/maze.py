for test_case in range(1):
    input()
    maze = [list(map(int, input())) for _ in range(16)]
    stack = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    si, sj, d = 1, 1, 0
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
                stack.append((si, sj, i))
                si, sj = si + dy[i], sj + dx[i]
        if maze[si+dy[d]][sj+dx[d]] != 1:
            si, sj = si + dy[d], sj + dx[d]
        else:
            si, sj, d = stack.pop(-1)
    print('#{} {}'.format(test_case, result))
