def q2(number):
    result = 1
    while number > 0:
        result *= number % 10
        number = number//10
    return result

print(q2(123))
print(q2(2020))
print(q2(123456789))