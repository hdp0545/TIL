def solution(n, results):
    answer = 0
    rank = [[set(), set()] for _ in range(n)]
    for result in results:
        a, b = result
        win, lose = rank[a-1], rank[b-1]
        win[0].add(b)
        lose[1].add(a)
        win[0] = win[0] | lose[0]
        lose[1] = lose[1] | win[1]
    flag = True
    while flag:
        flag = False
        for result in results:
            a, b = result
            win, lose = rank[a - 1], rank[b - 1]
            if flag == False and (win[0] != win[0] | lose[0] or lose[1] != win[1] | lose[1]):
                flag = True
            win[0] = win[0] | lose[0]
            lose[1] = lose[1] | win[1]
    for r in rank:
        if len(r[0]) + len(r[1]) == n - 1:
            answer += 1
    return answer

print(solution(5, [[1, 2], [4, 5], [3, 4], [2, 3]]), 5)
