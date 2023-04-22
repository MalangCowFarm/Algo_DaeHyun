from collections import deque

def solution(tickets):
    tickets.sort(key =lambda x : (x[0],x[1]))
    
    answer = []
    adj = [deque([]) for _ in range(10001)]
    visited = [[False]*(10001) for _ in range(10001)]
    air = {}
    # 공항 리스트 생성
    i =1
    for x,y in tickets :
        if air.get(x) == None :
            air[x] = i
            i+=1
        if air.get(y) == None :
            air[y] = i
            i+=1
    # 탐색 함수 생성
    def dfs(i) :
        if len(sol) > len(tickets) :
            return
        sol.append(i)
        if len(sol) == len(tickets) :
            for k in range(len(adj[i])) :
                if not visited[i][k] :
                    sol.append(adj[i][k])
                    return
        
        for k in range(len(adj[i])) :
            if not visited[i][k] :
                for j in range(len(adj[adj[i][k]])) :
                    if not visited[adj[i][k]][j] :
                        visited[i][k]= True
                        dfs(adj[i][k])

                    
                
                
    key = air['ICN']
    for x,y in tickets :
        adj[air[x]].append(air[y])

    
  
    for tc in range(len(adj[key])) :
        
        visited = [[False]*(10001) for _ in range(10001)]
        answer = []
        sol = []
        dfs(key)
    
        for i in sol :
            for k,v in air.items() :
                if v == i :
                    answer.append(k)

        if len(answer) == len(tickets)+1 :
            
            break
        else :
            first = adj[key].popleft()
            adj[key].append(first)
     
    return answer

