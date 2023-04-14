import sys

def DFS(graph,start,end,cnt) :
    global result
    visited[start] = True

    if start == end :
        result = cnt
    for i in range(People+1) :
        if graph[start][i] == 1 and not visited[i] :
            DFS(graph,i,end,cnt+1)

input = sys.stdin.readline

People = int(input())

A_num, B_num = map(int,input().split())

relation_cnt = int(input())

adj = [[0 for _ in range(People+1)] for _ in range(People+1)]
visited = [False] * (People+1)

for i in range(relation_cnt) :
    X,Y = map(int,input().split())
    adj[X][Y] = 1
    adj[Y][X] = 1

result, cnt = 0,0
DFS(adj,A_num,B_num,cnt)

if result != 0 :
    print(result)
else :
    print(-1)