for tc in range(1, int(input())+1):
    stick = input()
    i = 0
    result = 0
    height = 0
    while i < len(stick):
        if stick[i] == '(':
            result += 1
            height += 1
        else:
            if stick[i-1] == '(':
                result -= 1
                height -= 1
                result += height
            else:
                height -= 1
        i += 1
    print(f'#{tc} {result}')