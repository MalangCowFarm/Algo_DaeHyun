from collections import deque

def solution(maps):
    di = [-1,0,1,0]
    dj = [0,1,0,-1]
    
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    Q = deque([(0,0,1)])
    mini = 1e6
    while Q :
        i,j,cost = Q.popleft()

        if i == len(maps)-1 and j == len(maps[0])-1 :
            mini = min(mini,cost)
            break 
        for k in range(4) :
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<len(maps) and 0<=nj<len(maps[0]) and not visited[ni][nj] and maps[ni][nj] == 1 :
                visited[ni][nj] = True
                Q.append((ni,nj,cost+1))
    
    if mini == 1e6 :
        mini = -1
    
    return mini