def check(lis):
    if lis:
        return lis[-1]
    else:
        return None

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
        else:
            st.append(s)
    elif s in operator2:
        if check(st) in operator2:
            while check(st) != '(' and check(st) in operator1 and st:
                postfix.append(st.pop())
        else:
            st.append(s)
    else:
        postfix.append(s)

while st:
    postfix.append(st.pop())

print(''.join(map(str, postfix)))