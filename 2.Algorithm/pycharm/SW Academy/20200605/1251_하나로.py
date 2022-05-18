for tc in range(1, int(input())+1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    e = float(input())
    fee_list = [(i, j, e * ((x_list[i]-x_list[j])**2 + (y_list[i]-y_list[j])**2)) for i in range(N) for j in range(i + 1, N)]
    visit = [0] * N
    cnt = result = 0
    for gan in fee_list:
        if cnt >= N:
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
            for i in range(N):
                if visit[i] == a:
                    visit[i] = visit[gan[1]]
            result += gan[2]
            cnt += 1
    print(f'#{tc} {round(result)}')