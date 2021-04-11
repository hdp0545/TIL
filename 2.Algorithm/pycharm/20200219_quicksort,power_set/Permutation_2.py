def perm(arr, k, N):
    if k == N:
        print(arr)
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm(arr, k + 1, N)
            arr[k], arr[i] = arr[i], arr[k]
arr = [1, 3, 5, 7, 9]
perm(arr, 0, 5)