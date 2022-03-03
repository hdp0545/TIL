def solution(tickets):
    answer = []
    tickets_dic = {}
    for ticket in tickets:
        if ticket[0] in tickets_dic:
            tickets_dic[ticket[0]] = [ticket[1]]
        else:
            tickets_dic[ticket[0]].append(ticket[1])
    print()

    return answer