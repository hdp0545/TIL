def solution(n):
    stack = [i for i in range(2, n + 1)]
    visit = [True for _ in range(n + 1)]
    for n in stack:
        if visit[n]:

    return len(stack)

print(solution(10))