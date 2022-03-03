def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0

    temp = ''
    while n:
        temp += str(n % k)
        n = n // k
    temp = temp[::-1]

    chk = 0
    for idx, i in enumerate(temp):
        if i == '0':
            temp2 = temp[chk:idx]
            if temp2.isdigit():
                if is_prime(int(temp2)):
                    answer += 1
                chk = idx + 1
    try:
        if temp[-1] != '0':
            if is_prime(int(temp[chk:])):
                answer += 1
    except:
        return 1

    return answer