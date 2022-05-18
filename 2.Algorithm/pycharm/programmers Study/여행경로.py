
def solution(tickets):
    answer = []
    tickets.sort(reverse=True)
    tickets_dic = {}
    for ticket in tickets:
        if ticket[0] in tickets_dic:
            tickets_dic[ticket[0]].append(ticket[1])
        else:
            tickets_dic[ticket[0]] = [ticket[1]]
    stack = ['ICN']
    check = []
    temp = []
    last_temp = []
    while stack:
        visit = stack.pop()
        temp.append(visit)
        if visit in tickets_dic:
            if len(tickets_dic[visit]) != 1:
                check.append(visit)
                answer.append(temp)
                temp = []
            stack += tickets_dic[visit]
            del tickets_dic[visit]
        else:
            if check:
                if visit == check[-1]:
                    check.pop()
                    answer.append(temp)
                    temp = []
                else:
                    last_temp.append(temp)
                    temp = []
            else:
                answer.append(temp)
    return answer, last_temp, check

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))