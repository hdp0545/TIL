import heapq

def solution(food_times, k):
    N = len(food_times)
    k += 1
    stack = [[food_times[i], i] for i in range(N)]
    heapq.heapify(stack)
    t = 0
    while True:
        if stack:
            time, idx = heapq.heappop(stack)
            if k > N * (time - t):
                k -= N * (time - t)
                t = time
                N -= 1
            else:
                heapq.heappush(stack, [time, idx])
                break
        else:
            return -1
    k = k % N
    stack.sort(key=lambda x:x[1])
    return stack[k-1][1] + 1

print(solution([3, 1, 2], 5))