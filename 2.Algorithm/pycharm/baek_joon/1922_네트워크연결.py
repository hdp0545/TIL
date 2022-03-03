import heapq as hq

N = int(input())
M = int(input())
datas = [list(map(int, input().split())) for _ in range(M)]
answer = 0
ad_list = [[] for _ in range(N + 1)]
visit = [0] * (N+1)
for data in datas:
    a, b, c = data
    ad_list[a].append((c, b))
    ad_list[b].append((c, a))
heap = ad_list[1]
visit[1] = 1
hq.heapify(heap)
n = 1
for _ in range(N-1):
    while visit[n]:
        d, n = hq.heappop(heap)
    answer += d
    visit[n] = 1
    for i in ad_list[n]:
        hq.heappush(heap, i)
print(answer)