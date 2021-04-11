from itertools import permutations as pp

for tc in range(1, int(input())+1):
    N = int(input())
    data = list(map(int, input().split()))
    office = [data[0], data[1]]
    house = [data[2], data[3]]
    customers = [[data[2*i], data[2*i+1]] for i in range(2, N+2)]
    result = 2200
    for n_customers in pp(customers, len(customers)):
        start_x, start_y = office[0], office[1]
        temp = 0
        for customer in n_customers:
            temp += abs(customer[0] - start_x) + abs(customer[1] - start_y)
            start_x, start_y = customer[0], customer[1]
            # 백
            if temp > result:
                break
        else:
            temp += abs(house[0] - start_x) + abs(house[1] - start_y)
            if result > temp:
                result = temp
    print(f'{tc} {result}')
