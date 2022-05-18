for test_case in range(1, int(input()) + 1):
    data = input()
    s = []
    for d in data:
        if len(s) == 0:
            s.append(d)
        elif d == s[-1]:
            s.pop()
        else:
            s.append(d)
    print('#{} {}'.format(test_case, len(s)))