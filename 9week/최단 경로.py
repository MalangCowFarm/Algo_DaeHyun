import sys,heapq
input = sys.stdin.readline
INF = int(1e9)


v,e = map(int,input().split())

start =int(input())

adj = [[] for _ in range(v+1)]
distance = [INF]*(v+1)
for _ in range(e) :
    s,e,cost = map(int,input().split())
    adj[s].append((e,cost))


def dijkstra(start) :
    Q = []
    heapq.heappush(Q,(0,start))
    distance[start]= 0 
    while Q :
        dist, gets= heapq.heappop(Q)
        if distance[gets] < dist :
            continue

        for i in adj[gets] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(Q,(cost,i[0]))

dijkstra(start)


for i in range(1,v+1) :
    if i == start :
        print(0)
        continue
    if distance[i] == INF :
        print('INF')
    else :
        print(distance[i])
