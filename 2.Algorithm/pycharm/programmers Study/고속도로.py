import heapq

def solution(routes):
    answer = 1
    routes.sort()
    start = -30000
    end = 30000
    for route in routes:
        s, e = route
        if s <= end or start <= e:
            end = min(e, end)
            start = max(s, start)
        else:
            start = -30000
            end = 30000
            answer += 1
    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))