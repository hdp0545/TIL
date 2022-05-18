import sys
sys.stdin = open('work_input.txt', 'r')

for test_case in range(1, 11):
    V, E = map(int, input().split())
    gan_sun = list(map(int, input().split()))
    Ad_arr = [[0]*(V+1) for _ in range(V + 1)]
    visit = [0]*(V+1)
    stack = []
    result = []
    for i in range(E):
        Ad_arr[gan_sun[2 * i]][gan_sun[2 * i + 1]] = 1
    for j in range(1, V + 1):
        cnt = 0
        for i in range(1, V + 1):
            if Ad_arr[i][j] == 1:
                cnt += 1
        visit[j] = cnt
        if cnt == 0:
            stack.append(j)
    S = stack[-1]
    while stack:
        if visit[S] == 0:
            visit[S] = 1
            result.append(str(S))
        for i in range(V + 1):
            if Ad_arr[S][i] == 1:
                visit[i] -= 1
                if visit[i] == 0:
                    stack.append(i)
                    S = i
                    break
        else:
            S = stack.pop()
    print('#{} {}'.format(test_case, ' '.join(result)))