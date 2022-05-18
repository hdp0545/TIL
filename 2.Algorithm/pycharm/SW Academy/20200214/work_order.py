import sys
sys.stdin = open('work_input.txt', 'r')
sys.stdout = open('work_output1.txt', 'w')

for test_case in range(1, 11):
    V, E = map(int, input().split())
    gan_sun = list(map(int, input().split()))
    Ad_list = [[] for _ in range(V + 1)]
    visit = [0]*(V+1)
    stack = []
    result = []
    for i in range(E):
        Ad_list[gan_sun[2 * i]].append(gan_sun[2 * i + 1])
        visit[gan_sun[2 * i + 1]] += 1
    for j in range(1, V + 1):
        if visit[j] == 0:
            stack.append(j)
    while stack:
        S = stack.pop(-1)

        result.append(str(S))
        for i in Ad_list[S]:
            visit[i] -= 1
            if visit[i] == 0:
                stack.append(i)
    print('#{} {}'.format(test_case, ' '.join(result)))