def solution(k, num, links):
    N = len(num)
    num_sum = [0] * N
    parents = [-1] * N
    children = []
    for idx, link in enumerate(links):
        l, r = link
        if l == -1 and r == -1:
            children.append(idx)
        if l != -1:
            parents[l] = idx
        if r != -1:
            parents[r] = idx

    complete = [0] * N
    complete.append(1)
    while children:
        child = children.pop()
        num_sum[child] += num[child]
        parent = parents[child]
        if parent != -1:
            num_sum[parent] += num_sum[child]
            complete[child] = 1
            if complete[links[parent][0]] and complete[links[parent][1]]:
                children.append(parent)
    ancestors = [parents.index(-1)]
    answer_list = [parents.index(-1)]
    for _ in range(k-1):
        my_sum = 0
        for ancestor in ancestors:
            if my_sum < num_sum[ancestor]:
                max_ancestor = ancestor
                my_sum = num_sum[ancestor]
        my_max = my_sum
        stack = [max_ancestor]
        while stack:
            parent = stack.pop()
            l, r = links[parent]
            if l != -1 and r != -1:
                if num_sum[l] > num_sum[r]:
                    if my_max > max(num_sum[l], my_sum - num_sum[l]):
                        my_max = max(num_sum[l], my_sum - num_sum[l])
                        stack.append(l)
                    else:
                        ancestors.append(parents[l])
                        answer_list.append(parents[l])
                        temp = num_sum[parents[l]]
                        stack = [parents[l]]
                        while stack:
                            target = stack.pop()
                            if parents[target] != -1:
                                target = parents[target]
                                num_sum[target] -= temp
                                stack.append(target)
                        links[parents[parents[l]]][links[parents[parents[l]]].index(parents[l])] = -1
                        break
                else:
                    if my_max > max(num_sum[r], my_sum - num_sum[r]):
                        my_max = max(num_sum[r], my_sum - num_sum[r])
                        stack.append(r)
                    else:
                        ancestors.append(parents[r])
                        answer_list.append(parents[r])
                        temp = num_sum[parents[r]]
                        stack = [parents[r]]
                        while stack:
                            target = stack.pop()
                            if parents[target] != -1:
                                target = parents[target]
                                num_sum[target] -= temp
                                stack.append(target)
                        links[parents[parents[r]]][links[parents[parents[r]]].index(parents[r])] = -1
                        break
            elif l != -1:
                if my_max > max(num_sum[l], my_sum - num_sum[l]):
                    my_max = max(num_sum[l], my_sum - num_sum[l])
                    stack.append(l)
                else:
                    ancestors.append(parents[l])
                    answer_list.append(parents[l])
                    temp = num_sum[parents[l]]
                    stack = [parents[l]]
                    while stack:
                        target = stack.pop()
                        if parents[target] != -1:
                            target = parents[target]
                            num_sum[target] -= temp
                            stack.append(target)
                    links[parents[parents[l]]][links[parents[parents[l]]].index(parents[l])] = -1
                    break
            elif r != -1:
                if my_max > max(num_sum[r], my_sum - num_sum[r]):
                    my_max = max(num_sum[r], my_sum - num_sum[r])
                    stack.append(r)
                else:
                    ancestors.append(parents[r])
                    answer_list.append(parents[r])
                    temp = num_sum[parents[r]]
                    stack = [parents[r]]
                    while stack:
                        target = stack.pop()
                        if parents[target] != -1:
                            target = parents[target]
                            num_sum[target] -= temp
                            stack.append(target)
                    links[parents[parents[r]]][links[parents[parents[r]]].index(parents[r])] = -1
                    break
            else:
                answer_list.append(parent)
                temp = num_sum[parent]
                stack = [parent]
                while stack:
                    target = stack.pop()
                    if parents[target] != -1:
                        target = parents[target]
                        num_sum[target] -= temp
                        stack.append(target)
                links[parents[parent]][links[parents[parent]].index(parent)] = -1
    my_sum = 0
    for ancestor in answer_list:
        if my_sum < num_sum[ancestor]:
            my_sum = num_sum[ancestor]
    answer = my_sum


    return answer

print(solution(3, [1000, 1, 100, 10, 100], [[2, 1], [-1, -1], [4, 3], [-1, -1], [-1, -1]]))