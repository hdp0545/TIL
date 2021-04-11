for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A_costs = list(map(int, input().split()))
    B_judges = list(map(int, input().split()))
    temp = [0]*N
    result = 0
    for Bi in B_judges:
        for i in range(N):
            if Bi >= A_costs[i]:
                temp[i] += 1
                break
        if result < temp[i]:
            result = temp[i]
    print('#%d %d'%(tc, temp.index(result)+1))