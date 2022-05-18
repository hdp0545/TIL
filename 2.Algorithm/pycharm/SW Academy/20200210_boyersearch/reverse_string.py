a = 'algorithm'
b = a[::-1]
A = list(a)
for i in range(len(A) // 2):
    A[i], A[len(a) - 1 - i] = A[len(a) - 1 - i], A[i]
print(''.join(A))
print(b)