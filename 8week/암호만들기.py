import sys

input = sys.stdin.readline

def backtracks(i,Q) :
    if len(Q) >=2 :
        if ord(Q[-1]) <= ord(Q[-2]) :
            return 
    if len(Q) == L :
        cnt =0
        for x in consonant :
            if x in Q :
                cnt+=1
                
        if cnt ==0 or len(Q)-cnt < 2 :
            return
        else:
            res.append(Q)
        return           
    for i in range(C) :
        if not visited[i] :
            visited[i] = True
            Q+=Password[i]
            backtracks(i+1,Q)
            visited[i] = False 
            Q = Q[:len(Q)-1]

L,C = map(int,input().split())

Password = list(input().split())
visited = [False]*C
consonant = ['a','e','i','o','u']

Q = ''
res = []
backtracks(0,Q)
res = sorted(res)

for i in res :
    print(i)