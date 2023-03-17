import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline 

N = int(input())

Maps = [list(map(int,input().split())) for _ in range(N)]

visited = [[0 for _ in range(N)] for _ in range(N)]
mini = 1000
maxi = 0 
for i in range(N) :
    for j in range(N) :
        if Maps[i][j] > maxi :
            maxi = Maps[i][j]
        elif Maps[i][j] < mini :
            mini = Maps[i][j]


di = [0,1,0,-1]
dj = [1,0,-1,0]

def bfs_safe(i,j,cnt2) :
    Q = deque([(i,j)])
    visited[i][j] = cnt2


    while Q :
        x,y = Q.popleft()
        for k in range(4) :
            ni = x +di[k]
            nj = y +dj[k]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] != 1 and visited[ni][nj] != cnt2 :
                visited[ni][nj] = cnt2
                Q.append((ni,nj))

max_safe = 1
cnt = mini
cnt2 = 2

while cnt <= maxi :
    
    safe = 0
    for i in range(N) :
        for j in range(N) :
            if visited[i][j] !=1 and Maps[i][j] <=cnt :
                visited[i][j] = 1
                
                flag =True
                
                
    for i in range(N) :
        for j in range(N) :
            if visited[i][j] != 1 and visited[i][j] !=cnt2 :
                bfs_safe(i,j,cnt2)
                safe+=1
    
    max_safe = max(safe,max_safe)     
    
    cnt+=1      
    cnt2+=1

print(max_safe)

