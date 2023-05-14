import sys,copy
from pprint import pprint
from collections import deque
input = sys.stdin.readline 

## 사각형 끝까지 다 탐색하면서 백트래킹 하면 될 듯?

Maps = [list(map(int,input().split())) for _ in range(9)]

visited = [i for i in range(9)]


Q = deque()
for i in range(9) :
    for j in range(9) :
        if Maps[i][j] == 0 :
            Q.append((i,j))
        

# 체크하고 만약 후보가 될 수 있다면 큐에 추가하고 리턴 ex)3,4
def check(i,j,arr) :
    visits = [v for v in range(1,10)]
    candidate = []
    for x in range(9) :
        if x != j and arr[i][x] != 0 :
            visits[arr[i][x]-1] = 11
   
    for y in range(9) :
        if y != i and arr[y][j] != 0  :
            visits[arr[y][j]-1] = 11
    for a in range(i//3*3,i//3*3+3) :
        for b in range(j//3*3,j//3*3+3) :
            if a !=i and b !=j and arr[a][b] != 0 :
                visits[arr[a][b]-1] =11

    for t in range(9) :
        if visits[t] != 11 :
            candidate.append(visits[t])
   
    return candidate

def backtracks(wait,arr) :
    if not wait :
        
        for res in range(9) :
            print(*arr[res])
        exit(0)
    x,y = wait.popleft()
    for q in check(x,y,arr) :
        arr[x][y] = q
        backtracks(wait,arr)
        arr[x][y] = 0
    wait.appendleft((x,y))

backtracks(Q,Maps)
