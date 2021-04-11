answer = list()

def f(ans, result, k=0):
    if k == len(result):
        if len(set(ans)) == k:
            return set(ans)
        return
    for i in result[k]:
        ans.append(i)
        answer.append(f(ans, result, k+1))
        ans.pop()


def solution(user_id, banned_id):
    global answer
    result = []
    for id in banned_id:
        temp = []
        for user in user_id:
            if len(id) == len(user):
                for i, word in enumerate(id):
                    if word != '*' and word != user[i]:
                        break
                else:
                    temp.append(user)
        result.append(temp)
    ans = []
    f(ans, result)
    r = []
    c = 0
    for a in answer:
        if a not in r:
            r.append(a)
            c += 1
    return c - 1

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))