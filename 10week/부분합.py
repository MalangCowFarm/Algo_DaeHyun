import sys

input = sys.stdin.readline

n,m = map(int,input().split())

N_list = list(map(int,input().split()))

count = 0
interval_sum = 0
end = 0
flag = False
maxi = 10**10
cnt = 0
# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
     
    while interval_sum < m and end < n:
        interval_sum += N_list[end]
        cnt +=1 
        end += 1
    if interval_sum >= m:
        
        if cnt < maxi :
            maxi = cnt
            flag = True
    interval_sum -= N_list[start]
    cnt-=1
if flag :
    print(maxi)
else: 
    print(0)