def fibo(n):
    print("fibo(", n, ") is called")
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


memo = [0, 1]


def fibo1(n):
    global memo
    print("fibo1(", n, ") is called")
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]


def fibo2(n):
    f = [0, 1]
    print("fibo2(", n, ") is called")
    for i in range(2, n + 1):
        f.append(f[i-1] + f[i-2])
    return f[n]


print("recursive fibo")
fibo(7)
print()
print("recursive + memoization fibo")
fibo1(7)
print()
print("dynamic fibo")
fibo2(7)