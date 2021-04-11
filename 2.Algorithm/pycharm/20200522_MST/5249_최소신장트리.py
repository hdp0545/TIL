for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    result = 0
    cnt = 0
    visit = [0] * (V + 1)
    gans = [list(map(int, input().split())) for _ in range(E)]
    gans.sort(key=lambda x: x[2])
    cnt = 0
    for gan in gans:
        if cnt > V+1:
            break
        if visit[gan[0]] == 0 or visit[gan[1]] == 0:
            if visit[gan[0]] == 0 and visit[gan[1]] == 0:
                visit[gan[0]] = gan[1] + 1
                visit[gan[1]] = gan[1] + 1
            elif visit[gan[0]] == 0:
                visit[gan[0]] = visit[gan[1]]
            elif visit[gan[1]] == 0:
                visit[gan[1]] = visit[gan[0]]
            result += gan[2]
            cnt += 1

        elif visit[gan[0]] != visit[gan[1]]:
            a = visit[gan[0]]
            for i in range(V+1):
                if visit[i] == a:
                    visit[i] = visit[gan[1]]
            result += gan[2]
            cnt += 1

    print(f'#{tc} {result}')
