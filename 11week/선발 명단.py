import sys,copy

input = sys.stdin.readline 

T = int(input())

def backtracks(x,cnt) :
   
    global maxi
    if x == 11 :
        if cnt > maxi :
            maxi = cnt
        return
        
    for j in range(11) :
        if not visited[j] and Maps[x][j] != 0  :
            visited[j] = True
            backtracks(x+1,cnt+Maps[x][j])
            visited[j] = False
    return
for tc in range(T) :
    Maps = [list(map(int,input().split())) for _ in range(11)]
    maxi = 0 
    visited = [False]*11
    
    backtracks(0,0)
        
    print(maxi)