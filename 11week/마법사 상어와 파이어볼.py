import sys
from collections import deque

input = sys.stdin.readline 

## 방향 설정(8방향)
di = [-1,-1,0,1,1,1,0,-1]
dj = [0,1,1,1,0,-1,-1,-1]

# M은 파이어볼 개수, K는 second(명령 횟수)
N,M,K = map(int,input().split())

#0 배열 생성
Maps = [[[]*(N) for _ in range(N)] for _ in range(N)]


Q = deque()

for _ in range(M) :
    x,y,w,s,d = map(int,input().split())
    Q.append((x-1,y-1,w,s,d))


#움직이고 Maps에 배치
def move_collcate() :
    while Q :
        x,y,w,s,d = Q.popleft()
        nx = x + s*di[d] 
        ny = y + s*dj[d] 
        if 0<= nx < N and 0<= ny < N :
            Maps[nx][ny].append((nx,ny,w,s,d))
        else :

            if nx < 0 :
                if (nx +((abs(nx)//N)*(N))) ==  0 :
                    nx = 0
                else :
                    nx = N - abs(nx +((abs(nx)//N)*(N)))
            elif nx >= N : nx -= ((nx//N)*(N))
            if ny < 0 : 
                if (ny +((abs(ny)//N)*(N))) ==  0 :
                    ny = 0
                else :
                    ny = N - abs(ny +((abs(ny)//N)*(N)))
            elif ny >= N : ny -= ((ny//N)*(N))
           
            Maps[nx][ny].append((nx,ny,w,s,d))
             



# 합치고 다시 분리하기
def merge_separate() :
    for i in range(N) :
        for j in range(N) :
            if len(Maps[i][j]) >= 2 :
                s_w = s_s = f_c = odd_cnt = even_cnt = 0
                while Maps[i][j] :
                    a,b,w,s,d = Maps[i][j].pop()
                    s_w += w
                    s_s += s
                    f_c += 1
                    if d % 2 :
                        odd_cnt+=1
                    else :
                        even_cnt +=1
                if s_w < 5 :
                    continue
                s_w = s_w//5
                s_s = s_s//f_c
                if odd_cnt == 0 or even_cnt == 0 :
                    for x in [0,2,4,6] :
                        Q.append((i,j,s_w,s_s,x))
                            
                else :
                    for x in [1,3,5,7] :
                        Q.append((i,j,s_w,s_s,x))
            elif len(Maps[i][j]) == 1 :
                Q.append((i,j,Maps[i][j][0][2],Maps[i][j][0][3],Maps[i][j][0][4]))

for _ in range(K) :
    Maps = [[[]*(N) for _ in range(N)] for _ in range(N)]
    move_collcate()
    merge_separate()
    
res = 0
for i in Q :
    res += i[2]

print(res)
