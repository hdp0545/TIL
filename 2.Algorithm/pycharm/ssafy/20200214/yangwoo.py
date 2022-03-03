import sys
sys.stdin = open('work_input.txt', 'r')
sys.stdout = open('work_output2.txt', 'w')


def dfs(v):
    stack.append(v)
    while len(stack) > 0:
        v = stack.pop()
        temp = []
        for i in range(len(arr)):
            if arr[i][v] == 1 and visit[i] == 0:
                temp.append(i)
                stack.append(i)
        if len(temp) == 0:
            if visit[v] == 0:
                visit[v] = 1
                answer.append(v + 1)
            for w in range(V):
                if visit[w] == 0 and arr[v][w] == 1:
                    stack.append(w)


for test_case in range(10):
    V, E = map(int, input().split())
    G = list(map(int, input().split()))
    arr = [[0 for _ in range(V)] for _ in range(V)]
    for i in range(len(G) // 2):
        arr[G[2 * i] - 1][G[2 * i + 1] - 1] = 1
    stack = []
    visit = [0] * V
    answer = []
    dfs(2)
    answer = ' '.join(map(str, answer))
    print('#{} {}'.format(test_case + 1, answer))