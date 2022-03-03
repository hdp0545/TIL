import math

n, m = map(int, input().split())
x = int(math.sqrt(m)) + 1
prime_list = [True for _ in range(x + 1)]
prime_list[0] = False
prime_list[1] = False
for i in range(2, int(math.sqrt(x)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
    if prime_list[i] == True: # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= x:
            prime_list[i * j] = False
            j += 1
prime_numbers = []
for idx, value in enumerate(prime_list):
    if value:
        prime_numbers.append(idx * idx)

squared_list = [True for _ in range(m - n + 1)]
for square in prime_numbers:
    j = math.ceil(n / square)
    while square * j <= m:
        squared_list[square * j - n] = False
        j += 1
print(squared_list.count(True))

