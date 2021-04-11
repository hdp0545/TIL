def solution(priorities, location):
    answer = 0
    papers = [(idx, priority) for idx, priority in enumerate(priorities)]
    while papers:
        target = max(papers, key=lambda x: x[1])
        if target[0] == location:
            answer += 1
            break
        papers = papers[papers.index(target) + 1:] + papers[:papers.index(target)]
        answer += 1
    return answer




print(solution([1, 1, 9, 1, 1, 1], 0))