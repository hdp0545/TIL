import heapq

array = [6, 2, 3, 4, 5, 6]

for _ in range(10):
    heapq.heapify(array)
    print(array)