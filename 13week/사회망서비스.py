import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline 

N = int(input())

adj = [[] for _ in range(N+1)]
visited = [False]*(N+1)
dp = [[0,1] for _ in range(N+1)]
for _ in range(N-1) :
    x,y = map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

def tree(x) :
    
    
    visited[x] = True  
        
    for i in adj[x] :
        if not visited[i] :
            tree(i)
            dp[x][0] += dp[i][1]
            dp[x][1] += min(dp[i])
             
tree(1)
print(min(dp[1]))
