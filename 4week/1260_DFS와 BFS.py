import sys
from collections import deque

input = sys.stdin.readline

V, E, start = map(int, input().split())

adj = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)

for _ in range(E):
    r, c = map(int, input().split())
    adj[r].append(c)
    adj[c].append(r)


def dfs(node):
    if visited[node] == True:
        return
    print(node, end=" ")
    visited[node] = True
    adj[node] = sorted(adj[node])
    for i in adj[node]:
        if not visited[i]:
            dfs(i)


dfs(start)

sol = []


def bfs(node):
    queue = deque([node])
   
    visiteds = []
    while queue:
        node_now = queue.popleft()
        if node_now not in sol :
            sol.append(node_now)
        visiteds.append(node_now)
        
      
        for i in adj[node_now]:
            if i not in visiteds:
                queue.append(i)
                


bfs(start)

print("")
print(*sol)