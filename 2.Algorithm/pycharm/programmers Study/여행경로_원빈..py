def solution(tickets):
    tickets.sort()
    answer = []
    rawRoutes = ['ICN']

    def dfs(tickets, routes):
        nonlocal answer

        if len(tickets) == 0:
            tempArr = routes[:]
            answer.append(tempArr)
            return True

        crntLoc = routes[-1]
        for idx, ticket in enumerate(tickets):
            dep = ticket[0]
            arv = ticket[1]

            if dep == crntLoc:
                routes.append(arv)
                tempTickets = tickets[:]
                tempTickets.pop(idx)
                if dfs(tempTickets, routes):
                    return
                routes.pop()


    dfs(tickets, rawRoutes)
    return answer[0]