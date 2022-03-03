N, C = map(int, input().split())
houses = list([int(input()) for _ in range(N)])
houses.sort()
start = 1
end = houses[-1] - houses[0]
k = 1
while start < end:
    k = (end + start + 1) // 2
    temp = houses[0]
    cnt = 1
    for house in houses:
        if house >= temp + k:
            cnt += 1
            temp = house
            if cnt == C:
                start = k
                break
    if cnt < C:
        end = k - 1
print(start)