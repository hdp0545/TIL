for test_case in range(1, int(input())+1):
    string = input()
    N = len(string)
    result = ''
    for i in range(0, N -3, 3):
        for j in range(i+3, N, 3):
            if string[i:i+3] == string[j:j+3]:
                result = 'ERROR'
                break
        if result == 'ERROR':
            break
    else:
        cnt_dic = {'S' : 0, 'D' : 0, 'H' : 0, 'C' : 0}
        for i in range(0, N, 3):
            cnt_dic[string[i]] += 1
        result = '{} {} {} {}'.format(13 - cnt_dic['S'], 13 - cnt_dic['D'], 13 - cnt_dic['H'], 13 - cnt_dic['C'])
    print('#{} {}'.format(test_case, result))

