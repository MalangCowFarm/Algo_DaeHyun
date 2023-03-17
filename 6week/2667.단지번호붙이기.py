import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline 

N = int(input())

Maps = [list(map(int,input().rstrip())) for _ in range(N)]



visited = [[False for _ in range(N)] for _ in range(N)]


di = [0,1,0,-1]
dj = [1,0,-1,0]
def bfs(i,j,cnt) :
    Q = deque([(i,j)])
    visited[i][j] = True
    Maps[i][j] = cnt
    while Q :
        x,y = Q.popleft()
        for k in range(4) :
            ni = x + di[k]
            nj = y + dj[k]
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and Maps[ni][nj] == 1 :
                visited[ni][nj]= True
                Maps[ni][nj] = cnt
                Q.append((ni,nj))

res_dict = {}
cnt = 2
for i in range(N) :
    for j in range(N) :
        if not visited[i][j] and Maps[i][j] != 0:
            bfs(i,j,cnt)
            cnt +=1
          


for i in range(N) :
    for j in range(N) :
        if Maps[i][j] != 0 :
            if res_dict.get(Maps[i][j]) == None :
                res_dict[Maps[i][j]] = 1 
            else :
                res_dict[Maps[i][j]] +=1

res = []
print(len(res_dict))
for v in res_dict.values() :
    res.append(v)

res = sorted(res)
for i in res :
    print(i)
