def solution(histogram):
    answer = 0
    N = len(histogram)
    heigt_group = [[] for _ in range(10001)]
    for i in range(N):
        if heigt_group[histogram[i]] == []:
            heigt_group[histogram[i]] = [i, i]
        else:
            start, end = heigt_group[histogram[i]]
            if i < start:
                heigt_group[histogram[i]][0] = i
            elif end < i:
                heigt_group[histogram[i]][1] = i

    start = 100000
    end = 0
    for i in range(10000, -1, -1):
        heigt = heigt_group[i]
        if heigt:
            hs, he = heigt
            if start > hs:
                start = hs
            if end < he:
                end = he
            answer = max(answer, (end-start-1) * i)

    return answer

print(solution([2, 2, 2, 3]))