import sys
sys.stdin = open("input.txt", "r")

def bfs(v):
    visit = [0] * 101
    front = result = 0
    visit[v] = rear = 1
    q = [v]
    while front != rear:
        t = q[front]
        if visit[t] > visit[q[front-1]]:
            result = t
        else:
            if result < t:
                result = t
        for g in ad_list[t]:
            if not visit[g]:
                depth = visit[t] + 1
                visit[g] = depth
                q.append(g)
                rear += 1
        front += 1
    return result


for tc in range(1, 11):
    L, S = map(int, input().split())
    data = list(map(int, input().split()))
    ad_list = [[] for _ in range(101)]
    for i in range(0, L, 2):
        ad_list[data[i]].append(data[i+1])
    ad_list = list(map(lambda x: list(set(x)), ad_list))
    result = bfs(S)
    print('#{} {}'.format(tc, result))


