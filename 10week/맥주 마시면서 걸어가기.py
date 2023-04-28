import sys
from collections import deque
input = sys.stdin.readline

T =int(input())


def bfs(nums,i,j) :
    flag = False
    Q = deque()
    Q.append((0,i,j))
    visited[nums] = 1
    while Q :
     
        f_num,i,j = Q.popleft()
        if abs(end_x-i)+abs(end_y-j) <=1000 :
            flag = True 
            print('happy')
            break 
        for num,x,y in convenience :
            if  visited[num] == 0 and abs(x-i)+abs(y-j) <= 1000 :
                visited[num] = visited[f_num] +1
                Q.append((num,x,y))                
    if not flag :
        print('sad')
    return

for _ in range(T) :
    N = int(input())
    visited = [0]*(N+4)
    convenience = deque()
    home_x,home_y = map(int,input().split())
    for i in range(1,N+1) :
        con_x,con_y = map(int,input().split())
        convenience.append((i,con_x,con_y))
    end_x,end_y = map(int,input().split())

    bfs(0,home_x,home_y)    

