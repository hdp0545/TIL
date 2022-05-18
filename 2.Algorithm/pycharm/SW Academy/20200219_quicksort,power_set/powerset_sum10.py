a = [0] * 4
def backtrack(a, k, input):
    if k == input:
        print(a)
    else:
        k += 1
        a[k] = 1
        backtrack(a, k, input)
        a[k] = 0
        backtrack(a, k, input)
print(backtrack(a, 0, 3))