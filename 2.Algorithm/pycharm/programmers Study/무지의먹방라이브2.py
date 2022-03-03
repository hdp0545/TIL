from collections import deque as dq

def solution(food_times, k):
    list_a = []
    N = len(food_times)
    for idx, food in enumerate(food_times):
        list_a.append({
            "food": food,
            "next": idx + 1 if idx != len(food_times) - 1 else 0,
            "before": len(food_times) - 1 if idx == 0 else idx - 1
        })
    list_a.sort(key=lambda x:x["food"], reverse=True)
    cnt = 0
    while k:
        cnt += (list_a[-1]['food']-cnt)
        if cnt < (k / N):
            k -= cnt * N
            N -= 1
            obj = list_a.pop()


solution([3, 1, 2], 5)