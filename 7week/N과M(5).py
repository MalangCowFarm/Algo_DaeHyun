import sys

input = sys.stdin.readline

N,M =map(int,input().split())

N_list = sorted(list(map(int,input().split())))

checked = [False]*(N+1)
res = []


def dfs(number) :
    if number == M :
        print(*res)
        return
    
    for i in range(N) :
        if not checked[i] :
            res.append(N_list[i])
            checked[i] = True
            dfs(number+1)
            checked[i] = False
            res.pop()
            
dfs(0)