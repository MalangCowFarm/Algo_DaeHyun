import sys
from itertools import combinations
input = sys.stdin.readline


total, N = map(int,input().split())

Q = []

for _ in range(N) :
    cost,man = map(int,input().split())
    Q.append((cost,man))


dp = [1e6 for _ in range(total+100)]

dp[0] = 0

for cost,num_people in  Q :
    for i in range(num_people,total+100) :
        dp[i] = min(dp[i-num_people]+cost,dp[i])
        
print(min(dp[total:]))