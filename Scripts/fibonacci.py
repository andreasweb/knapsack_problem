def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fastFib(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        memo[n] = fastFib(n-1, memo) + fastFib(n-2, memo)
        return memo[n]

for i in range(400):
    print("fastFib(%s)" % str(i), fastFib(i))
