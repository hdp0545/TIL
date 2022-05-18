for tc in range(1, int(input())+1):
    num = input().split()[1]
    result = ''
    for x in num:
        n = ord(x)
        if 48 <= n <= 57:
            n -= 48
        else:
            n -= 55
        for i in range(3, -1, -1):
            if n & (1 << i):
                result += '1'
            else:
                result += '0'
    print('#{} {}'.format(tc, result))