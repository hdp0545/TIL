for test_case in range(1, int(input())+1):
    string = input()
    N = len(string)
    table = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
        'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
        'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
        '8', '9', '+', '/'
    ]
    code = ''
    result = ''
    for word in string:
        co = str(bin(table.index(word)))[2:]
        n = 6 - len(co)
        code += '0'*n + co
    print(code)
    for i in range(0, 6 * N, 8):
        code[i:i + 8]
