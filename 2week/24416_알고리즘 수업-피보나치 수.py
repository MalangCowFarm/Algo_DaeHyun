import sys

input = sys.stdin.readline
def fibo(n):
    if n == 1 or n == 2:
        return 1

    return fibo(n - 1) + fibo(n - 2)
def dp(n):
    dp_empty = [0] * (n + 1)
    dp_empty[0] = 1
    dp_empty[1] = 1

    dp_cnt = 0

    for i in range(3, n + 1):
        dp_cnt += 1
        dp_empty[n] = dp_empty[n - 1] + dp_empty[n - 2]

    return dp_cnt


T = int(input())

print(fibo(T), dp(T))