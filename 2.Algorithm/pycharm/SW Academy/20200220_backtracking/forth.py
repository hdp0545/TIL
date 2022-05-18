for test_case in range(1, int(input()) + 1):
    sik = input().split()
    operator = ['+', '-', '*', '/']
    i = 0
    st = []
    try:
        while sik[i] != '.':
            if sik[i] == '+':
                a = int(st.pop())
                b = int(st.pop())
                st.append(a + b)
            elif sik[i] == '-':
                a = int(st.pop())
                b = int(st.pop())
                st.append(b - a)
            elif sik[i] == '*':
                a = int(st.pop())
                b = int(st.pop())
                st.append(a * b)
            elif sik[i] == '/':
                a = int(st.pop())
                b = int(st.pop())
                st.append(b // a)
            else:
                st.append(sik[i])
            i += 1
    except:
        st = ['error']
    if len(st) != 1:
        st = ['error']
    print('#{} {}'.format(test_case, st.pop()))
