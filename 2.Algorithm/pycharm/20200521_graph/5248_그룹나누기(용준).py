# 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기
def find_parent(x):
    if x == node_list[x]:
        return x
    else:
        return find_parent(node_list[x])


def link_node(x, y):
    node_list[find_parent(y)] = find_parent(x)


for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    M_list = list(map(int, input().split()))
    node_list = [0] * (N+1)
    result = []
    for j in range(1, N+1):
        node_list[j] = j
    for i in range(M):
        start = M_list[2*i]
        end = M_list[2*i+1]
        link_node(start, end)
    for p in range(1, N+1):
        if find_parent(p) not in result:
            result.append(find_parent(p))
    print('#{} {}'.format(t, len(result)))