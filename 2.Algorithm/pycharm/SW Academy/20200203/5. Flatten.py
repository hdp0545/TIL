for test_case in range(1, 11):
    result = 0
    n = int(input)
    boxes = list(map(int, input().split()))
    boxes.sort()


    print('#{} {}'.format(test_case, result))