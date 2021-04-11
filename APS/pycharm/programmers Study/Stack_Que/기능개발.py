def solution(progresses, speeds):
    period = [(100 - progress) // speeds[idx] + int(bool((100 - progress) % speeds[idx])) for idx, progress in enumerate(progresses)]
    answer = []
    visit = [True] * len(period)
    for i in range(len(period)):
        if visit[i]:
            result = 0
            r = period[i]
            for j in range(i, len(period)):
                if period[j] <= r:
                    visit[j] = False
                    result += 1
            answer.append(result)
    return answer

print(solution([93,30,55], [1,30,5]))