import sys
sys.stdin = open('input_ladder.txt', 'r')

for t in range(1, 11):
    input()
    m = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]
    st = [s for s in range(102) if m[0][s]]
    i = st.index(m[99].index(2))
    for c in range(99, 0, -1):
        if m[c][st[i]+1] == 1:
            i += 1
        elif m[c][st[i]-1] == 1:
            i -= 1

    print('#{} {}'.format(t, st[i]-1))