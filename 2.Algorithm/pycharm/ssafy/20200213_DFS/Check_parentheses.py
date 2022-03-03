def pops(list, target=-1):
    if len(list) == 0:
        return
    else:
        r = list[target]
        del list[target]
        return r

for test_case in range(1, int(input())+1):
    test_word = input()
    open_parentheses = ['(', '{', '[', None]
    close_parentheses = [')', '}', ']']
    s = []


    for w in test_word:
        if w in open_parentheses:
            s.append(w)
        if w in close_parentheses:
            t = pops(s)
            if open_parentheses.index(t) != close_parentheses.index(w):
                print('#{} 0'.format(test_case))
                break
    else:
        if len(s):
            print('#{} 0'.format(test_case))
        else:
            print('#{} 1'.format(test_case))