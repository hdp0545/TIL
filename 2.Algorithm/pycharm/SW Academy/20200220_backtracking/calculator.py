def check(lis):
    if lis:
        return lis[-1]
    else:
        return None


for test_case in range(1, int(input()) + 1):
    input()
    sik = input()
    operator1 = ['+', '-']
    operator2 = ['*', '/']
    postfix = []
    st = []
    for s in sik:
        if s == '(':
            st.append(s)
        elif s == ')':
            while check(st) != '(':
                postfix.append(st.pop())
            st.pop()
        elif s in operator1:
            if check(st) in operator1 or check(st) in operator2:
                while check(st) != '(' and st:
                    postfix.append(st.pop())
                st.append(s)

        elif s in operator2:
            if check(st) in operator1:
                while check(st) != '(' and check(st) in operator1 and st:
                    postfix.append(st.pop())
            else:
                st.append(s)
        else:
            postfix.append(s)

    while st:
        postfix.append(st.pop())

    print(postfix)
    postfix.append('.')
    i = 0

    while postfix[i] != '.':
        if postfix[i] == '+':
            a = int(st.pop())
            b = int(st.pop())
            st.append(a + b)
        elif postfix[i] == '*':
            a = int(st.pop())
            b = int(st.pop())
            st.append(a * b)
        else:
            st.append(postfix[i])
        i += 1
    print('#{} {}'.format(test_case, st.pop()))