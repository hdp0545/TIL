def solution(food_times, k):
    dict = {}
    for idx, food in enumerate(food_times):
        dict[idx] = {
            "food" : food,
            "next" : idx + 1 if idx != len(food_times) - 1 else 0
        }
    before_t = len(food_times) - 1
    t = 0
    for i in range(k):
        if dict[t]["food"] > 1:
            dict[t]["food"] -= 1
            before_t = t
            t = dict[t]["next"]
        elif dict[t]["food"] == 1:
            dict[t]["food"] -= 1
            dict[before_t]["next"] = dict[t]["next"]
            if t == dict[t]["next"]:
                return -1
            t = dict[t]["next"]
    answer = t + 1
    return answer