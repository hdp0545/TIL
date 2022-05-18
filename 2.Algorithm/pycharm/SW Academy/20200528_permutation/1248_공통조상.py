def ancestors(target):
    stack = [target]
    while True:
        t = stack[-1]
        if reverse_list[t] == 0:
            return stack
        stack.append(reverse_list[t])


for tc in range(1, int(input())+1):
    V, E, target_1, target_2 = map(int, input().split())
    data = list(map(int, input().split()))
    ad_list = [[] for _ in range(V+1)]
    reverse_list = [0 for _ in range(V+1)]
    for i in range(0, 2*E, 2):
        ad_list[data[i]].append(data[i + 1])
        reverse_list[data[i + 1]] = data[i]
    target_1_ancestors = ancestors(target_1)
    target_2_ancestors = ancestors(target_2)
    for j in range(1, len(target_1_ancestors)+1):
        if target_1_ancestors[-1 * j] != target_2_ancestors[-1 * j]:
            ancestor = target_1_ancestors[-1 * j + 1]
            break
    st = [ancestor]
    result = 0
    while st:
        t = st.pop()
        result += 1
        for child in ad_list[t]:
            st.append(child)
    print(f'#{tc} {ancestor} {result}')