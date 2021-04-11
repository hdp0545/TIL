def solution(bridge_length, weight, truck_weights):
    answer = 0
    timer = [0] * len(truck_weights)
    sum_weight = 0
    start = end = 0
    while end != len(truck_weights):
        if timer[start] == bridge_length:
            sum_weight -= truck_weights[start]
            start += 1
        else:
            sum_weight += truck_weights[end]
            if sum_weight <= weight:
                end += 1
                for i in range(start, end):
                    timer[i] += 1
                answer += 1
            else:
                sum_weight -= truck_weights[end]
                time = bridge_length - timer[start]
                for i in range(start, end):
                    timer[i] += time
                answer += time
    return answer + bridge_length

print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))