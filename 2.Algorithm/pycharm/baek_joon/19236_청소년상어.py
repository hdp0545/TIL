import pprint

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1, -1, -1, 0, 1, 1, 1, 0, -1]


def fish(matrix):
    target_fish = 1
    while target_fish < 17:
        matrix = f(matrix, target_fish)
        target_fish += 1
    return


def f(matrix, target_fish):
    for i in range(4):
        for j in range(4):
            if matrix[i][j][0] == target_fish:
                d = matrix[i][j][1]
                for _ in range(8):
                    if 0 <= i + dy[d] < 4 and 0 <= j + dx[d] < 4 and matrix[i + dy[d]][j + dx[d]][0] != 17:
                        if d <= 8:
                            matrix[i][j][1] = d
                        else:
                            matrix[i][j][1] = d - 8
                        matrix[i][j], matrix[i + dy[d]][j + dx[d]] = matrix[i + dy[d]][j + dx[d]], matrix[i][j]
                        return matrix
                    else:
                        d += 1
    return matrix


def shark_stat(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j][0] == 17:
                return (i, j, matrix[i][j][1])


raw_data = [list(map(int, input().split())) for _ in range(4)]
data = [[[i[2*j], i[2*j+1]] for j in range(4)] for i in raw_data]
data[0][0][0] = 17
fish(data)
print(data)

stack = [[[data[i][j][:] for i in range(4) for j in range(4)], data[0][0][0]]]
result = data[0][0][0]
while stack:
    data, count = stack.pop()
    if result < count:
        result = count
    y, x, d= shark_stat(data)
    for i in range(1, 4):
        if 0 <= y+(i*dy[d]) < 4 and 0 <= x+(i*dx[d]) < 4:
            pass

