T = int(input())

sol = []
for testcase in range(T) :
    sol.append(int(input()))
dp = [0 for _ in range(T)] ## 계단 오를때 최대값을 지속적으로 갱신해야 하므로 0배열 생성

if T <= 2 :
    if T == 1 :
        dp[0] = sol[0] #dp[0]은 인풋리스트의 0번 인덱스로 설정

        print(sol[0])
    elif T == 2:
        dp[1] = sol[0]+sol[1]
        print(sol[0]+sol[1])
else :
    dp[0] = sol[0]
    dp[1] = sol[0]+sol[1]
    dp[2] = max(sol[0]+sol[2],sol[1]+sol[2])
    for i in range(3,T) :
        dp[i] = max(dp[i-2]+sol[i],dp[i-3]+sol[i-1]+sol[i])
        # 계단은 3칸 이상 올라갈 수 없고, 마지막은 꼭 밝아야한다는 규칙을 기억하자
        # 매 계단마다 최대값을 갱신시키면서 dp리스트에 추가해준다.