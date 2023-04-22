import sys
input = sys.stdin.readline

N = int(input())

Q = []
## 맨 앞에는 무조건 나머지랑 다른색깔로 칠해야함
for _ in range(N) :
    red,green,blue = map(int,input().split())
    Q.append((red,green,blue))

mini = INF =  1e9

for i in range(3) : # R,G,B를 각각 처음 집으로 하는 반복문
    dp = [[INF,INF,INF] for _ in range(N)] # dp값을 최대로 만든다. 최소값을 갱신하고, 2번째 집에서 첫번째 집의 색깔을 다시 선택하지 않게 하기 위해 모두 INF로 시작
    dp[0][i] = Q[0][i] # 첫번째 집 색깔에 따른 가중치를 dp[0]에 할당
    for j in range(1,N) : # 1~N번까지 돌리면서 바로 이전 색깔과 다른 색깔의 가중치와 이전까지의 가중치를 더해가며 갱신한다.  
        dp[j][0] = Q[j][0] + min(dp[j-1][1],dp[j-1][2])
        dp[j][1] = Q[j][1] + min(dp[j-1][0],dp[j-1][2])
        dp[j][2] = Q[j][2] + min(dp[j-1][0],dp[j-1][1])
    
    for k in range(3) : # DP의 N-1행에서 [X,Y,Z]로 가중치가 모두 더해진 값들이 모여있을 것이다. 그렇다면 여기서 시작 색깔인 i와 마지막 색깔 중 하나인 k와 일치하지 않고, 현재까지 저장된 최소값보다 작다면 갱신하면 된다
        if i != k and dp[N-1][k] < mini :
            mini = dp[N-1][k]

print(mini) 
