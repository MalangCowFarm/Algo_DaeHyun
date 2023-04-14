import sys

input = sys.stdin.readline


def DFS(graph, start):
    global cnt

    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            cnt += 1
            DFS(graph, i)


V = int(input())
E = int(input())

adj = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)

for _ in range(E):
    r, c = map(int, input().split())
    adj[r].append(c)
    adj[c].append(r)

cnt = 0
DFS(adj, 1)

print(cnt)