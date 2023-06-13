import sys
from pprint import pprint
input = sys.stdin.readline

N,M = map(int,input().split())

K = int(input())


Maps = [[[0,0,0,[]] for _ in range(N+1)] for _ in range(M+1)]

Maps[M][0] = [0,1,1,[]]
k = -1
for _ in range(K) :
    a,b,c,d = map(int,input().split())
    Maps[M-b][a][0] = -1
    Maps[M-d][c][0] = -1
    Maps[M-b][a][3].append(k)
    Maps[M-d][c][3].append(k)
    k-=1
for i in range(M,-1,-1) :
    for j in range(N+1) :

        if 0<=i+1<=M and 0<=i<=M :
            Maps[i][j][2] += Maps[i+1][j][2]
            Maps[i][j][1] += Maps[i+1][j][1]
        if 0<=j-1<=N and 0<=j<=N :

            Maps[i][j][2] += Maps[i][j-1][2]
            Maps[i][j][1] += Maps[i][j-1][1]


        if Maps[i][j][0] == -1:
            if 0<=i-1<=M and Maps[i-1][j][0] == -1  :
                for x in Maps[i-1][j][3] :
                    if x in Maps[i][j][3] :
                        if 0<=j+1<=N :
                            flag = False
                            for w in Maps[i][j+1][3] : 
                                if w in Maps[i][j][3] :
                                    flag = True
                            
                            if not flag :
                                Maps[i][j+1][2] += Maps[i][j][2]
                                Maps[i][j+1][1] += Maps[i][j][1]
                        Maps[i][j][2] = 0
                        Maps[i][j][1] = 0 
                        
                    
            if 0<=j+1<=N and Maps[i][j+1][0] == -1 :
                for y in Maps[i][j+1][3] :
                    if y in Maps[i][j][3] :
                        
                        if 0<=i-1<=M : 
                            flag = False
                            for t in Maps[i-1][j][3] :
                                if t in Maps[i][j][3] :
                                    flag = True 
                                

                            if not flag :
                                Maps[i-1][j][1] += Maps[i][j][1]
                                Maps[i-1][j][2] += Maps[i][j][2]
                        Maps[i][j][1] = 0 
                        Maps[i][j][2] = 0
                      



print(max(Maps[0][N][1],Maps[0][N][2]))

