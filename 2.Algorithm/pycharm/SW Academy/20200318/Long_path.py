T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    in_list = [[] for _ in range(N + 1)]
    result = 0
    for i in range(M):
        s, e = map(int, input().split())
        in_list[s].append(e)
        in_list[e].append(s)

    for i in range(1, N+1):
        visit = [0] * (N + 1)
        stack = [i]
        visit[i] = 1
        while stack:
            if result < len(stack):
                result = len(stack)
            for j in in_list[i]:
                if visit[j] == 0:
                    visit[j] = 1
                    i = j
                    stack.append(j)
                    break
            else:
                i = stack.pop()
    print("#{} {}".format(tc, result))