N, C = map(int, input().split())
houses = list(map(int, [input() for _ in range(N)]))
houses.sort()
dists = [[houses[i] - houses[i-1], i] for i in range(1, N)]
min_dist = houses[-1] - houses[0]
for _ in range(N - C):
    min_dist = 1000000000
    idx = 0
    nidx = 0
    i = 0
    while i < N-2:
        dist, next = dists[i]
        ndist, nnext = dists[next]
        if min_dist > dist + ndist:
            min_dist = dist + ndist
            idx = i
            fail = next
            nidx = nnext
        i = next
    dists[idx] = [min_dist, nidx]
print(min_dist)