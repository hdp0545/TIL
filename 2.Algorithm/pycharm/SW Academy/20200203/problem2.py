arr = [-2, 2, 3, 5, 7, 8, 9, 10, 1, -10]
n = len(arr)
results = []
for i in range(1, 1 << n):
    result = 0
    for j in range(n):
        if i & (1 << j):
            result += arr[j]
    results.append(result)
if 0 in results:
    print('0 존재')
else:
    print('0없음')