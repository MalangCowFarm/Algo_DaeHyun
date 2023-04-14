import sys
from collections import deque
input = sys.stdin.readline
delta = [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,-2],[2,-1],[2,1],[1,2]]
def bfs(i,j,depth) :
    global mini
    # print(i,j,depth,mini)
    
    Q = deque([(i,j,0)])

    visited[i][j] = True

    while Q : 
        x,y,depth = Q.popleft()
        if x==es and y == ee :
            if depth < mini :
                mini = depth
            return 
        for k in range(8) :
            nx = x + delta[k][0]
            ny = y + delta[k][1]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and Maps[nx][ny] ==0 :
                Maps[nx][ny] = depth+1
                Q.append((nx,ny,depth+1))
                



       
 

# and ((es-i)**2+(ee-j)**2) > ((es-ni)**2+(ee-nj)**2)


T =int(input())

for _ in range(T) :
    N = int(input())
    Maps = [[0 for _ in range(N)] for _ in range(N)]
    ss,se = map(int,input().split())
    es,ee = map(int,input().split())
   
    #함수실행
    mini = 10**10
    visited = [[False for _ in range(N)] for _ in range(N)]
    bfs(ss,se,0)

    print(mini)