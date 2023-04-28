import sys

input = sys.stdin.readline

di = [-1,0,1,0]
dj = [0,1,0,-1]


R,C =map(int,input().split())

Maps = [list(input().rstrip()) for _ in range(R)]

visited = [0]*100



maxi = 1
def backtracks(i,j,depth) :
   
    global maxi
    if depth > maxi : 
        maxi = depth
        
    for k in range(4) :
        ni = i +di[k]
        nj = j +dj[k]
        
        if 0<=ni<R and 0<=nj<C :
            temp = ord(Maps[ni][nj])
            if visited[temp]==0 :
                visited[temp] = 1
                backtracks(ni,nj,depth+1)
                visited[temp] = 0

    return

visited[ord(Maps[0][0])] = 1 
backtracks(0,0,1)

print(maxi)

