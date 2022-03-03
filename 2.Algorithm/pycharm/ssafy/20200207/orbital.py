def shap(tuple_a, tuple_b):
    x, y = tuple_a
    c, d = tuple_b
    a = x + c
    b = y + d
    n = (((a + b - 1)*(a + b)) // 2) - b + 1
    return n

def pahs(n):
    sample = 1
    while n > ((sample + 1) * sample) // 2:
        sample += 1
    m = (((sample + 1) * sample) // 2) - n
    return sample - m, m + 1


for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    print('#{} {}'.format(test_case, shap(pahs(N), pahs(M))))