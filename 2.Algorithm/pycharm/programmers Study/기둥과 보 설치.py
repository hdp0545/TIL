def solution(n, build_frame):
    answer = []
    visit = [[0] * (n + 1) for _ in range(n + 1)]
    for order in build_frame:
        x, y, a, b = order
        if b:
            if a == 0:
                if y == 0 or visit[x][y]:
                    answer.append([x, y, a])
                    visit[x][y + 1] = 1
            else:
                if visit[x][y] == 1:
                    answer.append([x, y, a])
                    visit[x+1][y] = 2
                elif visit[x+1][y] == 1:
                    answer.append([x, y, a])
                    visit[x][y] = 2
                elif (visit[x][y] == 2 and visit[x+1][y] == 2):
                    answer.append([x, y, a])
        else:
            if a == 0:


    return answer

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))