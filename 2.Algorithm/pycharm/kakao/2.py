def solution(s):
    answer = []
    i = 1
    tuple_list = []
    while i < len(s):
        if s[i] == '{':
            stack = set()
            i += 1
            w = ''
            while s[i] != '}':
                if s[i] != ',':
                    w += s[i]
                else:
                    stack.add(int(w))
                    w = ''
                i += 1
            stack.add(int(w))
            tuple_list.append(stack)
        i += 1
    tuple_list.sort(key=lambda x: len(x))
    tup_0 = set()
    for tup in tuple_list:
        a = tup - tup_0
        answer.append(a.pop())
        tup_0 = tup
    return answer

print(solution(	"{{2},{2,1},{2,1,3},{2,1,3,4}}"))

s = "{{2},{2,1},{2,1,3},{2,11,3,4}}"

