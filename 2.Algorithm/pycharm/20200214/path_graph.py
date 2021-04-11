for test_case in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    input_list = [[] for _ in range(V + 1)]
    stack = []
    visit = [0]*(V+1)
    for _ in range(E):
        st, wt = map(int, input().split())
        input_list[st].append(wt)

    S, G = map(int, input().split())
    stack.append(S)
    result = 0
    while stack:
        if S == G:
            result = 1
            break
        if visit[S] == 0:
            visit[S] = 1
        for i in input_list[S]:
            if visit[i] == 0:
                stack.append(i)
                S = i
                break
        else:
            S = stack.pop(-1)
    print('#{} {}'.format(test_case, result))