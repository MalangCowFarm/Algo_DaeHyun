import sys
from collections import deque

input = sys.stdin.readline

def dfs(array) :
    maxi = 0
    Q = array
    di = [0,1,0,-1,0,0]
    dj = [1,0,-1,0,0,0]
    dz = [0,0,0,0,-1,1]
    while Q :
        x,y,z = Q.popleft()
        for k in range(6) :
            ni = x+di[k]
            nj = y+dj[k]
            nz = z+dz[k]
            if 0<=ni<N and 0<=nj<M and 0<=nz<level and visited[nz][ni][nj] == 0 and Maps[nz][ni][nj] == 0  :
                Q.append((ni,nj,nz))
                Maps[nz][ni][nj] = 1
                visited[nz][ni][nj] = visited[z][x][y]+1
    if zero_count == 0:
        print(0)
        return
    for i in visited :
        for j in i :
            for v in j :
                maxi = max(v,maxi)
                if v == 0 :
                    print(-1)
                    return
    print(maxi-1)
    return

M,N,level = map(int,input().split()) # N은 i M은 j

Maps = [[list(map(int,input().split())) for _ in range(N)] for _ in range(level)]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(level)]

Qs = deque()
zero_count = 0
for l in range(level) :
    for i in range(N) :
        for j in range(M) :
            if Maps[l][i][j] == 1 :
                  Qs.append((i,j,l))
                  visited[l][i][j] = 1
            elif Maps[l][i][j] == 0 :
                zero_count += 1

            elif Maps[l][i][j] == -1 :
                visited[l][i][j] = -1

dfs(Qs)
