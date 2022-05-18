import random

N = 10000000
leng = 300000
arr = []
for _ in range(100):
    arr.append(random.randrange(1, 251))
print(arr)
random.shuffle(arr)

print(arr)