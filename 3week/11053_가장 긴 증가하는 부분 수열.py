import sys

input = sys.stdin.readline

N = int(input())

N_list = (list(map(int, input().split())))

dp = [1] * (N + 1)  ## 개수 기억

for i in range(1, N):
    for j in range(i):
        if N_list[i] > N_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
