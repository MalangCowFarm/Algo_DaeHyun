N = int(input())

num = list(map(int,input().split()))

solution =0

cnt = 0
for i in range(N) :
    for j in range(1,num[i]+1) :
        if num[i] == 1 :
            cnt -=1
        
        if num[i] % j == 0 :
            cnt+=1
        else : 
            pass
    if cnt == 2 :
        solution +=1
    else :
        pass
    cnt=0



print(solution)
