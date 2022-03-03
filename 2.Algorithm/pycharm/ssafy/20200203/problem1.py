a = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
result = 0
for i in range(5):
    for j in range(5):
        for _ in range(4):
            new_i = i+dx[_]
            new_j = j+dy[_]
            if new_i in range(5) and new_j in range(5):
                result += abs(a[new_i][new_j] - a[i][j])

print(result)