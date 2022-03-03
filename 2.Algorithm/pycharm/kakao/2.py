from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def calc_distance(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                que = deque()
                que.append((i, j))
                lv = 0
                visit = [[0] * 5 for _ in range(5)]
                while que and lv < 2:
                    i, j = que.popleft()
                    visit[i][j] = 1
                    for k in range(4):
                        ni, nj = i+dy[k], j+dx[k]
                        if 0 <= ni < 5 and 0 <= nj < 5:
                            if place[ni][nj] == 'O' and visit[ni][nj] == 0:
                                que.append((ni, nj))
                            elif place[ni][nj] == 'P' and visit[ni][nj] == 0:
                                return 0
                    lv += 1
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(calc_distance(list(map(list, place))))
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))