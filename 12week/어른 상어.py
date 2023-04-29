import sys
from collections import deque
input = sys.stdin.readline

N,M,K = map(int,input().split())

Maps = [list(map(int,input().split())) for _ in range(N)]

dir = [(-1,0),(1,0),(0,-1),(0,1)]

dir_Q = list(map(int,input().split()))
for i in range(len(dir_Q)) :
    dir_Q[i] = dir_Q[i]-1
shark_Q =deque()
for i in range(N) :
    for j in range(N) :
        if Maps[i][j] != 0 :
            shark_Q.append((Maps[i][j],i,j,dir_Q[Maps[i][j]-1]))
            Maps[i][j] = (Maps[i][j],K)
            
prior_Q = [[] for _ in range(M)]

for i in range(M) :
    for k in range(1,5) :
        one,two,three,four = map(int,input().split())
        prior_Q[i].append((one-1,two-1,three-1,four-1))


def move(arr) :
    length = len(shark_Q)
    while length > 0 :
        shark_num,x,y,direction = shark_Q.popleft()
        nx = x + dir[direction][0]
        ny = y + dir[direction][1]
        if 0<=nx<N and 0<=ny<N :
            if arr[nx][ny] == 0 :
                arr[nx][ny] = (shark_num,K)
                shark_Q.append((shark_num,nx,ny,direction))
            elif arr[nx][ny][0] != shark_num :
                if shark_num < arr[nx][ny][0] :
                    for v in range(len(shark_Q)) :
                        if shark_Q[v][0] == arr[nx][ny][0] :
                            shark_Q[v] = (shark_num,nx,ny,direction)
                            break
                    arr[nx][ny] = (shark_num,K)
            elif arr[nx][ny][0] == shark_num :
                arr[nx][ny] = (shark_num,K)
                shark_Q.append((shark_num,nx,ny,direction))
        length-=1
    return arr   

def position(arr) :
    for x in range(len(shark_Q)) :
        shark,i,j,direct = shark_Q.popleft()
        cnt = 0
        empty_Q = []
        for k in range(4) :
            ni = i +dir[k][0]
            nj = j +dir[k][1]
          
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0 :
                empty_Q.append(k)

        if len(empty_Q) > 1 :
            for t in prior_Q[shark-1][direct] :
                
                if t in empty_Q :
                    direct = t 
                    break                     
        elif len(empty_Q) == 1 :
            direct = empty_Q[0]
        else :
            empty_Q = []
            for k in range(4) :
                ni = i +dir[k][0]
                nj = j +dir[k][1]
                if 0<=ni<N and 0<=nj<N and arr[ni][nj][0] == shark :
                    empty_Q.append(k)
            if len(empty_Q) > 1 :
                
                for t in prior_Q[shark-1][direct] :
                    if t in empty_Q :
                        direct = t
                        break                     
            elif len(empty_Q) == 1 :
                direct = empty_Q[0]
        
        shark_Q.append((shark,i,j,direct))
    return arr

def erase(arr) :
    for i in range(N) :
        for j in range(N) :
            if arr[i][j] != 0 :
                if arr[i][j][1] == 1 :
                    arr[i][j] = 0 
                else :
                    arr[i][j] = (arr[i][j][0],arr[i][j][1]-1)
cnt = 0
while len(shark_Q) > 1 :
    if cnt >= 1000 :
        cnt = -1
        break 
    cnt+=1
    position(Maps)
    erase(Maps)
    move(Maps)

print(cnt)