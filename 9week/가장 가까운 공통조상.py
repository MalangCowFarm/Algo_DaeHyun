import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

def DFS(graph,start,res) :
    if visited[start] ==  True :
        return res
    res.append(start)
    visited[start] = True



    for i in graph[start] :
        if not visited[i] :
            DFS(graph,i,res)


for _ in range(T) :
    V = int(input())
    E = V-1
    visited = [False] * (V + 1)
    adj = [[] for _ in range(V+1)]
    for _ in range(E) :
        r,c = map(int,input().split())
        adj[c].append(r)
        
    
    result1 = []
    result2 = []
    a_node,b_node = map(int,input().split())
    DFS(adj,a_node,result1)
    visited = [False] * (V + 1)
    DFS(adj,b_node,result2)
    
    for i in result2 :
        if i in result1 :
            print(i)
            break