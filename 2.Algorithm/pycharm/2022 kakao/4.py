import heapq

def solution(n, info):
    appeach_score = 0
    lion_score = 0
    cnt = 0
    heap = []
    answer = [0] * 11
    for i in range(11):
        if info[i]:
            appeach_score += (10 - i)

    for i in range(11):
        if info[i]:
            score = (10 - i) * 2
        else:
            score = (10 - i)
        expect_score = score / (info[i] + 1)
        heapq.heappush(heap, (-expect_score, i, info[i] + 1))

    for _ in range(11):
        expect_score, i, value = heapq.heappop(heap)
        cnt += value
        if info[i]:
            score = (10 - i) * 2
        else:
            score = (10 - i)
        lion_score += score
        answer[i] = value
        if n - cnt == 0:
            break
        elif n - cnt < 0:
            lion_score -= score
            answer[i] = 0
            cnt -= value



    if n - cnt == 0:
        if lion_score <= appeach_score:
            answer = [-1]
        return answer
    else:
        answer[10] = n - cnt
        return answer

print(solution(10, [8, 10, 1, 2, 3, 10, 10, 10, 0, 0, 0]))