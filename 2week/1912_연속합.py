import sys

input = sys.stdin.readline

N = int(input())

N_list = list(map(int,input().split()))

dp_list = [0 for _ in range(N)] # dp에 활용할 0배열 생성

dp_list[0] = N_list[0]  #<- dp의 0번 인덱스에 input_list 0번 값을 넣음

for i in range(N-1) :
    dp_list[i+1] = max(dp_list[i]+N_list[i+1],N_list[i+1]) # dp의 다음 인덱스 값은 리스트+이전dp값과 리스트값을 비교하여 더 큰 것으로 선정함

print(max(dp_list))