N = int(input())

num = list(map(int,input().split()))

solution =0

count = 0
for i in range(N) :
    for j in range(1,num[i]+1) :
        if num[i] == 1 :
            count -=1
        
        if num[i] % j == 0 :
            count+=1
        else : 
            pass
    if count == 2 :
        solution +=1
    else :
        pass
    count=0



print(solution)
