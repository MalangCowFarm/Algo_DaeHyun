import sys

input = sys.stdin.readline 

INF = 1e9

N = int(input())
M = int(input())


adj = [[INF]*(N+1) for _ in range(N+1)]
tc = [[()]*(N+1) for _ in range(N+1)]


for i in range(1,N+1) :
    adj[i][i] = 0 

for _ in range(M) :
    s,e,cost = map(int,input().split())
    adj[s][e] = min(adj[s][e],cost)
    tc[s][e] = (s,e)

for k in range(1,N+1) :
    for a in range(1,N+1) :
        for b in range(1,N+1) :
            if adj[a][b] > adj[a][k] + adj[k][b] :
                adj[a][b] = adj[a][k]+adj[k][b]
                tc[a][b] = tc[a][k] + tc[k][b][1:]
           


for i in range(1,N+1) :
    line = []
    for j in range(1,N+1) :
        if adj[i][j] == INF :
            line.append(0)
        else :
            line.append(adj[i][j])
    print(*line)

for i in range(1,N+1) :
    for j in range(1,N+1) :
        print(len(tc[i][j]), *tc[i][j])