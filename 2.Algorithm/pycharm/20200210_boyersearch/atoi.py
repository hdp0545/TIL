def atoi(string):
    result = 0
    for s in string:
        if ord('0') <= ord(s) <= ord('9'):
            digit = ord(s) - ord('0')
            result = result * 10 + digit
        else:
            result = '숫자가 아닙니다.'
            break
    return result


def itoa(a):
    sr = ''
    while True:
        r = a % 10
        sr = sr+chr(r + ord('0'))
        a //= 10
        if a == 0: break
    s = ''
    for i in range(len(sr) - 1, -1, -1):
        s = s + sr[i]
    return s


print(atoi('689'))
print(atoi('a000'))

