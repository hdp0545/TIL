target = input()
result = N = len(target)
while N > 0:
    N -= 1
    if not(target[N].isalpha()):
        N -= 1
        result -= 1
        if target[N-1:N+1] == 'dz':
            N -= 1
            result -= 1
    elif target[N-1:N+1] == 'lj' or target[N-1:N+1] == 'nj':
        N -= 1
        result -= 1

print(result)