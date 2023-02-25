import sys
sys.setrecursionlimit(10000)



def DFS(graph,start) :
    visited[start] =1

    for i in graph[start] :
          if not visited[i] :
                DFS(graph,i)



input = sys.stdin.readline

V, E = map(int,input().split())

visited = [False] * (V+1)
adj = [[] for _ in range(V+1)]

for _ in range(E) :
    r,c = map(int,input().split())
    adj[r].append(c)
    adj[c].append(r)
cnt= 0

for i in range(1,V+1) :
    if not visited[i] :
        DFS(adj,i)
        cnt+=1
print(cnt)

