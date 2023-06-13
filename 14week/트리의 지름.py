import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())

adj = [[] for _ in range(N+1)]

for _ in range(N-1) :
    a,b,cost = map(int,input().split())
    adj[a].append((b,cost))
    adj[b].append((a,cost))


def dfs(node,cost) :
    for x,y in adj[node] :
        cal = cost + y
        if visited[x] == -1 :  
            visited[x] = cal
            dfs(x,cal)

    return


visited = [-1]*(N+1)
visited[1] = 0 

dfs(1,0)
idx=tmp=0

for i in range(1,N+1) :
    if visited[i] > tmp :
        tmp = visited[i]
        idx = i

visited = [-1]*(N+1)
visited[idx] = 0
dfs(idx,0)

print(max(visited))

