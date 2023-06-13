import sys
input = sys.stdin.readline

total, N = map(int,input().split())


Q = []
for _ in range(N) :
    cost,man = map(int,input().split())
    Q.append((cost,man))


dp = [1e6 for _ in range(total+100)]

dp[0] = 0 

for cost,man in Q :
    for i in range(man,total+100) :
        dp[i] = min(dp[i],dp[i-man]+cost)


print(min(dp[total:]))