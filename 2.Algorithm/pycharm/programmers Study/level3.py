from collections import deque as que

def solution(n, edge):
    ad_list = [[] for _ in range(n + 1)]
    for gan in edge:
        a, b = gan
        ad_list[a].append(b)
        ad_list[b].append(a)
    visit = [0] * (n + 1)
    q = que([1])
    nq = que([])
    cnt = 0
    visit[1] = 1
    answer = 0
    while q:
        v = q.popleft()
        for target in ad_list[v]:
            if not visit[target]:
                nq.append(target)
                visit[target] = 1
                cnt += 1
        if not q:
            q = nq.copy()
            nq.clear()
            if q:
                answer = cnt
                cnt = 0
    return answer



print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))