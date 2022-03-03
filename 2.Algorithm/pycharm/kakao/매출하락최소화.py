def solution(sales, links):
    answer = 0
    N = len(sales)
    ad_list = [[] for _ in range(N)]
    leaders = []
    for link in links:
        a, b = link
        ad_list[a - 1].append(b)
        leaders.append(a - 1)

    return answer

print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))