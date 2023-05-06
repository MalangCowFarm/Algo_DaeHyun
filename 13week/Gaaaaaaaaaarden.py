import sys,copy
from itertools import combinations
from pprint import pprint
from collections import deque
input = sys.stdin.readline 

N,M,G,R = map(int,input().split())

# 0 = 호수 , 1= 배양액 불가능 땅, 2= 배양액 가능 땅, 3 ="green" , 4 = "red"
Maps = [list(map(int,input().split())) for _ in range(N)]

di = [-1,0,1,0]
dj = [0,1,0,-1]

def check(arr) :
    res = 0 
    checking =  []
    Mapp = [[[0,0] for _ in range(M)] for _ in range(N)]
  
    for i in range(len(empty)) :
        Mapp[empty[i][0]][empty[i][1]] = [-1,-1]
    
    for i in range(len(arr)) :
        Mapp[arr[i][0]][arr[i][1]] = [arr[i][2],0]
    while arr :
        x,y,color,sec = arr.popleft()
        if Mapp[x][y][0] == 7 :
           
            if (x,y) not in checking :
                checking.append((x,y))
                res+=1
            continue
        

        for k in range(4) :
            nx = x+di[k]
            ny = y+dj[k]
            if 0<=nx<N and 0<=ny<M and (Mapp[nx][ny][0] == 0 or (Mapp[nx][ny][0] == 7-color and Mapp[nx][ny][1] ==sec+1)) :
                    Mapp[nx][ny][0] += Mapp[x][y][0]
                    Mapp[nx][ny][1] = sec+1
                    arr.append((nx,ny,color,sec+1))                
    
    return res
   
possible = deque()
empty = []
for i in range(N) :
    for j in range(M) :
        if Maps[i][j] == 2 :
            possible.append((i,j))
        elif Maps[i][j] == 0 :
            empty.append((i,j))
# G적용 
maxi = 0
for i in combinations(possible,G) :
    wait =deque()
    possible_c = copy.deepcopy(possible)
    t = len(i)
    k = 0 
    while k < len(i) :
        possible_c.remove((i[k][0],i[k][1])) 
        wait.append((i[k][0],i[k][1],3,0))        
        k+=1
    for j in combinations(possible_c,R) :
        wait_c = copy.deepcopy(wait)
        t = len(j)
        k = 0 
        while k < len(j) :
            wait_c.append((j[k][0],j[k][1],4,0))
            k+=1
        maxi = max(maxi,check(wait_c))
        # check하기

print(maxi)