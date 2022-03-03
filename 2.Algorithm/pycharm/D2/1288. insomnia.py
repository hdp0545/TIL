for test_case in range(1, int(input())+1):
    N = int(input())
    set_ = set()
    cnt = 1
    while set_ != {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
        words = str(cnt*N)
        for word in words:
            set_.add(word)
        cnt += 1
    cnt -= 1
    print('#{} {}'.format(test_case, cnt*N))
