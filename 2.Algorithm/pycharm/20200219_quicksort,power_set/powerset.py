a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def backtrack(a, k, input, value, result=[], cnt=0):

    if cnt == value:
        print(result)

    elif k == input:
        return
    else:
        if cnt > value:
            return
        else:
            k += 1
            result.append(a[k])
            cnt += k
            backtrack(a, k, input, value, result, cnt)
            cnt -= k
            del result[-1]
            backtrack(a, k, input, value, result, cnt)


backtrack(a, 0, 10, 10)