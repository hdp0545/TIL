Ns = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for _ in range(int(input())):
    t, N = input().split()
    print(t)
    N_list = list(input().split())
    c = [0]*10
    for i in N_list: c[Ns.index(i)] += 1
    b = [Ns[i]*c[i] for i in range(10)]
    print(' '.join(b))

