from collections import deque

def solution(input_text):
    orders = list(input_text.split('\n'))
    result = ''
    M, N = 0, 0
    cnt = 0
    cnt_log = deque()
    day_cnt = 0
    pandan = True
    for idx, order in enumerate(orders):
        if idx:
            if order == 'SHOW':
                if pandan:
                    if cnt < N:
                        result += '1\n'
                        cnt += 1
                    else:
                        result += '0\n'
                        cnt = 0
                        pandan = False
                else:
                    result += '0\n'
            elif order == 'NEGATIVE':
                pandan = False
            elif order == 'NEXT':
                day_cnt += 1
                if pandan:
                    cnt_log.append(cnt - cnt_log[-1])
                    if len(cnt_log) > M:
                        cnt -= cnt_log.popleft()
                else:
                    if day_cnt > M:
                        day_cnt = 0
                        pandan = True
                        cnt = 0
                        cnt_log.clear()
            elif order == 'EXIT':
                result += 'BYE\n'
            else:
                result += 'ERROR\n'
        else:
            result += order
            M, N = map(int, order.split(' '))
    return result