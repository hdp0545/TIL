import heapq

def solution(abilities, k):
    N = len(abilities)
    abilities.sort(reverse=True)
    n = (N + 1) // 2
    heap = []
    answer = 0
    for i in range(n):
        i *= 2
        if i + 1 < N:
            heapq.heappush(heap, abilities[i+1]-abilities[i])
            answer += abilities[i + 1]
        else:
            heapq.heappush(heap, -abilities[i])
    for _ in range(k):
        temp = heapq.heappop(heap)
        answer -= temp
    return answer


print(solution([2, 8, 3, 6, 1, 9, 1, 9], 2))