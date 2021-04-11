for tc in range(1, int(input())+1):
    N = int(input())
    data = list(map(int, input().split()))
    sum = 0
    result = data[0]
    for d in data:
        if d >= 0:
            sum += d
        else:
            if result < sum:
                result = sum
            if sum * -1 < d:
                sum += d
            else:
                sum = 0
    if result < sum:
        result = sum
    print('#%d %d'%(tc, result))