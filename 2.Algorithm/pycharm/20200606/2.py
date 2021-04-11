def cnt(li, num):
    result = 0
    for item in li:
        result += item // num
    return result

N, M = map(int, input().split())
data = [float(input()) for _ in range(N)]
sum_data = sum(data)
max1 = round(sum_data / M, 2)
while M > cnt(data, max1):
    max1 -= 1
max1 += 1
while M > cnt(data, max1):
    max1 -= 0.1
max1 += 0.1
while M > cnt(data, max1):
    max1 -= 0.01
max1 += 0.01
while M > cnt(data, max1):
    max1 -= 0.001
print('%.2f' % round(max1, 2))