def backtrack(a, k, input):
    if sum([i * a[i] for i in range(1, 11)]) > 10:
        return
    if k == input:
        print(a, sum([i * a[i] for i in range(1, 11)]))
    else:
        k += 1
        for i in range(2):
            a[k] = i
            backtrack(a, k, input)
a = [0] * 11
backtrack(a, 0, 10)