def f(s, depth):
    global result
    if s >= result:
        return result
    if depth == N and result > s:
        return s
    else:
        for i in range(N):
            if not visit[i]:
                visit[i] = 1
                result = f(s+table[depth][i], depth+1)
                visit[i] = 0
    return result


for t in range(1, int(input())+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    visit = [0]*N
    result = N*99
    f(0, 0)
    print('#{} {}'.format(t, result))

