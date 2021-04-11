for tc in range(1, int(input()) + 1):
    data = float(input())
    result = ''
    n = 1
    while n < 13:
        data *= 2
        if data == 1:
            result += '1'
            print('#{} {}'.format(tc, result))
            break
        else:
            if data > 1:
                data -= 1
                result += '1'
            else:
                result += '0'
        n += 1
    else:
        print(f'#{tc} overflow')