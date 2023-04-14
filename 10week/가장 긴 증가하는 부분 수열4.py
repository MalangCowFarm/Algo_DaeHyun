import sys
input = sys.stdin.readline


N = int(input())
N_list= list(map(int,input().split()))
dp = [1]*(N)
for i in range(1,N) :
    for j in range(i) :
        if N_list[i] > N_list[j] :
           dp[i] = max(dp[i],dp[j]+1)



print(max(dp))


res = []
r = max(dp)


for i in range(N-1,-1,-1) :
    if dp[i] == r :
        res.append(N_list[i])
        r-=1

print(*res[::-1])
                