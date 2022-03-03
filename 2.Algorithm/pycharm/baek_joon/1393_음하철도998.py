g_x, g_y = map(int, input().split())
s_x, s_y, v_x, v_y = map(int, input().split())
q = max(abs(v_x), abs(v_y))
r = min(abs(v_x), abs(v_y))
if r == 0:
    r = q
else:
    max_n = q % r
    while max_n != 0:
        max_n = q % r
        q = r
        r = max_n
v_x, v_y = v_x // r, v_y // r
result = 80000
for t in range(200):
    d = (g_x - (s_x + t * v_x)) ** 2 + (g_y - (s_y + t * v_y)) ** 2
    if d < result:
        result = d
    else:
        break
print(s_x + (t-1) * v_x, s_y + (t-1) * v_y)