p = input()
t = input()
M = len(p)
N = len(t)

def Bruteforce(p, t):
    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == M:
        return t[i - M:i]
    else:
        return -1

print(Bruteforce(p, t))