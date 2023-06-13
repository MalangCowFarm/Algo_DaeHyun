import sys

input = sys.stdin.readline 

T = int(input())

for _ in range(T) :
    x,y = map(int,input().split())
    if x > y : 
        x,y = y,x 
    elif x == y :
        print(0)
        continue
    N = y-x
    n = 1;cnt =0 
    while N > 0 : 
        if N>=2*n :
           
            N-= 2*n 
            n+=1
            cnt += 2
        else :
            while N != 0  :
                if N >= n :
                    N -= n
                    cnt +=  1
                else :
                    N = 0
                    cnt +=1 
                    break
                    
        
    print(cnt)