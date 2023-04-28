import sys
from pprint import pprint
from collections import deque

di = [-1,0,1,0]
dj = [0,1,0,-1] 

input = sys.stdin.readline

N,M =map(int,input().split())

Maps = [list(map(int,input().split())) for _ in range(N)]

visited = [[False]*M for _ in range(N)]

def find(parent,x) :
    if parent[x] == x :
        return x
    parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b) :
    rootA = find(parent,a)
    rootB = find(parent,b)
    if rootA < rootB :
        parent[rootB] = rootA
    else :
        parent[rootA] = rootB

def check(i,j) :
    start = Maps[i][j]
    for k in range(4) :
        cnt = 0 
        ni = i +di[k]
        nj = j +dj[k]
        if 0<= ni < N and 0<= nj < M and Maps[ni][nj] == 0 :
            while 0<=ni<N and 0<=nj<M and Maps[ni][nj] != Maps[i][j]:
                
                if Maps[ni][nj] != 0  :
                    end = Maps[ni][nj]
                    if cnt >= 2  :
                        
                        waiting.append((cnt,start,end))
                    break
                cnt += 1
                ni  += di[k]
                nj  += dj[k]
def bfs(i,j) :
    Q = deque([(i,j)])
    visited[i][j] = True 

    while Q :
        x,y = Q.popleft()
        Maps[x][y] = nums
        for k in range(4) :
            nx = x + di[k]
            ny = y + dj[k]
            if 0<= nx < N and 0<= ny < M and not visited[nx][ny] and Maps[nx][ny] == 1 :
                visited[nx][ny] = True
                Q.append((nx,ny))
island = nums = 0 
for i in range(N) :
    for j in range(M) :
        if not visited[i][j] and Maps[i][j] == 1 :
            nums += 1
            bfs(i,j)
            island +=1

parent = [0]* (island+1)

for i in range(island+1) :
    parent[i] = i

waiting = []


for i in range(N) :
    for j in range(M) :
        if Maps[i][j] != 0 :
            check(i,j)

waiting.sort()

res = 0 
for cnt,a,b in waiting :
    if find(parent,a) != find(parent,b) :
        union(parent,a,b)
        res += cnt

flag = False

for i in range(1,island) :
    
    if find(parent,i) != find(parent,i+1) :
        flag = True
        print(-1)
        break

if not flag :
    print(res)    