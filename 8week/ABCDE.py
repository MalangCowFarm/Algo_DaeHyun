import sys

input = sys.stdin.readline 


Man,relation = map(int,input().split())

adj = [[] for _ in range(Man+1)]
for _ in range(relation) :
    r,c = map(int,input().split())
    adj[r].append(c)
    adj[c].append(r)
    

result = []

def dfs(start,second) :
    
    global cnt
    if second >= 4 :
        cnt = 1
        return
    if visited[start] == True :
        return
  
    
    for i in adj[start] :
        if not visited[i] :
            visited[start] = True
            dfs(i,second+1)
            visited[start] = False

for i in range(Man) :
    cnt = 0 
    visited = [False for _ in range(Man+1)]
    second = 0
    dfs(i,0)
    
    if cnt == 1  :
        print(1)
        break

if cnt != 1  :
    print(0)
