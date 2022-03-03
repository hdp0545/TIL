import heapq

answer = []
N = int(input())
works = []
for i in range(N):
    t, a = map(int, input().split())
    works.append((t, a, i))
works.sort(key=lambda x: x[1])
t, a, i = works.pop(0)
heap = [(t, a, i)]
time = a
for work in works:
    t, a, i = work
    tt, ta, ti = heapq.heappop(heap)
    tt -= a - time
    time = a
    if tt > 0:
        heapq.heappush(heap, (tt, ta, ti))
    else:
        answer.append(ti)
    heapq.heappush(heap, work)
while heap:
    answer.append(heapq.heappop(heap)[2])
print(answer)
