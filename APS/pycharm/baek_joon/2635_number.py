N = int(input())
real_result = []

for A in range(1, N + 1):
    result = [N, A]
    while True:
        result.append(result[-2] - result[-1])
        if result[-1] < 0:
            break
    del result[-1]
    if len(result) > len(real_result):
        real_result = result

print(len(real_result))
print(' '.join(map(str, real_result)))