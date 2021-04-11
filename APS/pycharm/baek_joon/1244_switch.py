def change(switch, i):
    if switch[i] == 1:
        return 0
    else:
        return 1

N = int(input())
switch = list(map(int, input().split()))
s_num = int(input())

for _ in range(s_num):
    G, C = map(int, input().split())
    if G == 1:
        for i in range(N):
            if (i + 1) % C == 0:
                switch[i] = change(switch, i)


    else:
        switch[C-1] = change(switch, C-1)
        n = 1
        while True:
            if not(0 <= (C-1) + n <= N-1 and 0 <= (C-1) - n <= N-1):
                break
            elif switch[C - 1 + n] != switch[C - 1 - n]:
                break
            else:
                if switch[C-1 + n] == 1:
                    switch[C-1 + n] = 0
                else:
                    switch[C-1 + n] = 1
                if switch[C - 1 - n] == 1:
                    switch[C - 1 - n] = 0
                else:
                    switch[C - 1 - n] = 1
                n += 1
nn = 0
while True:
    print(' '.join(map(str, switch[nn:nn + 20])))
    nn += 20
    if nn > N:
        break