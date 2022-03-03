def Counting_Sort(A, B, k):
    C = [0] * k

    for i in range(0, len(B)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i-1]

    for i in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

    return B

