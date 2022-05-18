from queue import PriorityQueue as pq

def idx(string):
    result = 0
    for s in string:
        result = result << 1
        if s == 'o':
            result += 1
    return result


N, M = map(int, input().split())
ad_matrix = [[0] * (1 << N) for _ in range(1 << N)]
for _ in range(M):
    temp = input().split()
    ad_matrix[idx(temp[0])][idx(temp[1])] = int(temp[2])
print(ad_matrix)
q = int(input())
for _ in range(q):
    temp = input().split()
    s, e = map(idx, temp)
    djikstra = [float('inf')] * (1 << N)
    que = pq()
    que.put((0, s))
    djikstra[s] = 0
    result = -1
    while not que.empty():
        d, ns = que.get()
        if d > djikstra[e]:
            break
        if ns == e:
            result = d
            break
        for i, value in enumerate(ad_matrix[ns]):
            if value:
                nd = d + value
                if djikstra[i] > nd:
                    djikstra[i] = nd
                    que.put((nd, i))
    print(result)


