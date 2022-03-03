def peek(s) :
    if len(s) == 0:
        return
    else:
        return s[-1]


def pop(s) :
    if len(s) == 0:
        return
    else:
        return s.pop(-1)


def push(s, item):
    s.append(item)
    return

