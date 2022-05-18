from collections import deque

def solution(n, vertex):
    ad_list = [[] for _ in range(n + 1)]
    for v in vertex:
        a, b = v
        ad_list[a].append(b)
        ad_list[b].append(a)
    visit = [False] * (n + 1)
    visit[1] = True
    stack = deque()
    stack.append([1, 0])
    md = 0
    answer = 0
    while stack:
        s, d = stack.popleft()
        if md == d:
            answer += 1
        if md < d:
            md = d
            answer = 1
        for n in ad_list[s]:
            if visit[n] == False:
                stack.append([n, d+1])
                visit[n] = True
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))