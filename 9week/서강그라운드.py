import sys
from pprint import pprint
input = sys.stdin.readline

INF = 1e9

N,M,R = map(int,input().split())


graph = [[INF]*(N+1) for _ in range(N+1)]

N_list = list(map(int,input().split()))

for _ in range(R) :
    a,b,cost = map(int,input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1],cost)
    graph[b-1][a-1] = min(graph[b-1][a-1], cost)


for k in range(N) :
    for a in range(N) :
        for b in range(N) :
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
            if a==b :
                graph[a][b] = 0 

maxi = 0
for a in range(N) :
    result = 0
    for b in range(N) :
            if graph[a][b] <= M :
                result += N_list[b]
    maxi = max(maxi,result)
pprint(maxi)