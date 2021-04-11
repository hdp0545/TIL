import datetime

def matching(keyosk, time, dur):
    keyosk[1] = time + datetime.timedelta(minutes=dur)
    keyosk[2] += dur
    keyosk[3] += 1
    return keyosk



def solution(n ,customers):
    answer = 0
    keyosks = [[i, 0, 0, 0] for i in range(n)]
    for customer in customers:
        flag = True
        day, ar_time, dur = customer.split(' ')
        dur = int(dur)
        arrive_time = datetime.datetime.strptime(day + ar_time, '%m/%d%H:%M:%S')
        unused_keyosk_stack = []
        for keyosk in keyosks:
            i, end_time, duration, cnt = keyosk
            if end_time == 0:
                keyosk = matching(keyosk, arrive_time, dur)
                flag = False
                break
            timedelta = arrive_time - end_time
            if timedelta.days > 0:
                unused_keyosk_stack.append(keyosk)
        if unused_keyosk_stack and flag:
            keyosk = min(unused_keyosk_stack, key=lambda x:arrive_time - x[1])
            number = keyosk[0]
            keyosks[number] = matching(keyosk, arrive_time, dur)
            flag = False
        elif flag:
            keyosk = min(keyosks, key=lambda x: x[1])
            number, end_time, dur, cnt = keyosk
            keyosks[number] = matching(keyosk, end_time, dur)
            flag = False
    return max(keyosks, key=lambda x:x[3])[3]

print(solution(3, ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]))