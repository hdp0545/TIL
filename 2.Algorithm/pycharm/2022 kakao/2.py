import math

def isPrime(n):
    if n < 2:
        return False
    if n==2:
        return True
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    p = ''
    while n > 0:
        t = n % k
        if t:
            p = str(t) + p
        else:
            if p:
                if isPrime(int(p)):
                    answer += 1
                p = ''
        n //= k
    if isPrime(int(p)):
        answer += 1

    return answer

print(solution(4905, 10))