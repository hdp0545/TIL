def solution(l1, l2):
    tank_small = min(l1, l2)
    tank_large = max(l1, l2)
    visit = [0 for _ in range(tank_large+1)]
    i = tank_large
    result = []
    while visit[i] == 0:
        visit[i] = 1
        i -= tank_small
        if i <= 0:
            i += tank_large
    for idx, value in enumerate(visit):
        if value == 1:
            result.append(idx)
    return result
print(solution(50, 38))