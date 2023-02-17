import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def DFS(graph,start) :
   visited[start] = True

   for i in graph[start] :
        if not visited[i] :
            DFS(graph,i)


V,E = map(int,input().split())

adj = [[] for _ in range(V+1)]
visited = [False for _ in range(V+1)]

for i in range(E) :
    r,c = map(int,input().split())
    adj[r].append(c)
    adj[c].append(r)

cnt = 0

for i in range(1,V+1) :
    if not visited[i] :
        DFS(adj,i)
        cnt+=1


print(cnt)