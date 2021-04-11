def paper(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    else:
        return paper(N-10) + paper(N-20)


for t in range(1, int(input())+1):
    print('#{} {}'.format(t, paper(int(input()))))