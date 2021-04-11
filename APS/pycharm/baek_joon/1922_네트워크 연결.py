N = int(input())
visit = [0] * (N + 1)
M = int(input())
data = [list(map(int, input().split())) for _ in range(M)]
data.sort(key=lambda x: x[2])
cnt = 0
result = 0
for link in data:
    if cnt > N+1:
        break
    if visit[link[0]] == 0 or visit[link[1]] == 0:
        if visit[link[0]] == 0 and visit[link[1]] == 0:
            visit[link[0]] = link[1] + 1
            visit[link[1]] = link[1] + 1
        elif visit[link[0]] == 0:
            visit[link[0]] = visit[link[1]]
        elif visit[link[1]] == 0:
            visit[link[1]] = visit[link[0]]
        result += link[2]
        cnt += 1
    elif visit[link[0]] != visit[link[1]]:
        a = visit[link[0]]
        for i in range(N+1):
            if visit[i] == a:
                visit[i] = visit[link[1]]
        result += link[2]
        cnt += 1
print(result)