import sys

input = sys.stdin.readline 
sys.setrecursionlimit(10**6)

def dfs(i,j) :
    k = 0 
    visited[i][j] = 1
    di = [1,0,-1,0]
    dj = [0,1,0,-1]
    for t in range(4) :
        ni = i+di[k]
        nj = j+dj[k]
        if 0<=ni< H and 0<= nj < W and visited[ni][nj] == 0 and zero_list[ni][nj] == 1 :
            visited[ni][nj] = 1
            dfs(ni,nj)
        k+=1


T = int(input())

for testcase in range(T) :
    W,H,K = map(int,input().split())

    zero_list = [[0 for _ in range(W)] for _ in range(H)]
    visited = [[0 for _ in range(W)] for _ in range(H)]
    for _ in range(K) :
        r,c = map(int,input().split())
        zero_list[c][r] =1

    cnt = 0
    for x in range(H) :
        for y in range(W) :
            if visited[x][y] == 0 and zero_list[x][y] == 1 :
                dfs(x,y)
                cnt+=1


    print(cnt)
                
               
                            
