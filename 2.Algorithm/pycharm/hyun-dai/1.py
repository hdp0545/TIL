from itertools import permutations

def solution(k, m):
    datas = [i for i in range(1, k+1)]
    result = 0
    for data in permutations(datas, k):
        target = int(''.join(map(str, data)))
        if(target % m == 0):
            result += 1
    return result


print(solution(9, 1))