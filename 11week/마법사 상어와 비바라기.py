import sys
from pprint import pprint
from collections import deque
input = sys.stdin.readline 

##방향 지정
di = [0,-1,-1,-1,0,1,1,1]
dj = [-1,-1,0,1,1,1,0,-1]


N, M = map(int,input().split())

Maps = [list(map(int,input().split())) for _ in range(N)]

#이동 저장
moving = deque()
for _ in range(M) :
    d, s = map(int,input().split())
    moving.append((d,s))

#구름 위치 저장
cloud = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]

diagonal = [(-1,-1),(-1,1),(1,1),(1,-1)]

#움직임
def move_grow() :
    global cloud
    copys = deque()
    cloud_copy = []
    visited = [[False]*N for _ in range(N)]
    dir,spe = moving.popleft()
    while cloud :
        i,j = cloud.pop()
        ni = (N +i + spe*di[dir-1])%N
        nj = (N + j + spe*dj[dir-1])%N
       
        
        visited[ni][nj] = True
        copys.append((ni,nj))
        cloud_copy.append((ni,nj))
        Maps[ni][nj] +=1
    
    while copys :
        cnt = 0
        x,y = copys.popleft()
        for k in range(4) :
            ni = x + diagonal[k][0]
            nj = y + diagonal[k][1]
            if 0<=ni<N and 0<=nj<N :
                if Maps[ni][nj] >= 1 :
                    cnt +=1
        
        Maps[x][y] += cnt
    
    for i in range(N) :
        for j in range(N) :
            if Maps[i][j] >= 2 and not visited[i][j] :
                Maps[i][j] -=2
                cloud.append((i,j))  


while moving :
    move_grow()

 
   
res = 0
for i in range(N) :
    for j in range(N) :
        res += Maps[i][j]


print(res)
