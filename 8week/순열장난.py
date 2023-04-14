import sys

input = sys.stdin.readline

N = input().rstrip()

if len(N) > 9 :
    M = (len(N)-9)//2 + 9

else : 
    M = len(N)

visited = [False]*(M+1)

res = []
print(len(N))
print(M)
i =0
while i < len(N) :
    print(i,"아이")
    X = int(N[i:i+2]) 
    Y = int(N[i])
    if 0<= X <= M and not visited[int(N[i:i+2])] :
        res.append(N[i:i+2])
        visited[int(N[i:i+2])] = True
        i+=1
    
    else : 
       
        if 1<=Y<=M and not visited[int(N[i])] : 
            visited[int(N[i])] = True
            res.append(N[i])


    i+=1


for i in res :
    print(int(i),end=" ")


