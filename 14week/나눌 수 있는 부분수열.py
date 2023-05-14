import sys

input = sys.stdin.readline

T =int(input())

for _ in range(T) :
    d,n = map(int,input().split())
    N_list = list(map(int,input().split()))
    mod_list = [0] * d
    cnt = sum = 0

    for N in N_list :
        sum = (sum +N) % d
        cnt += mod_list[sum]
        mod_list[sum] +=1

        if sum == 0 :
            cnt +=1
   
   
    print(cnt)