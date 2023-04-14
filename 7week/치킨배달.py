import sys
from collections import deque
from itertools import combinations
import copy
input = sys.stdin.readline

#r = i , c = j
## 치킨집 좌표 Q에 등록한다 , 1일때 치킨거리 구함 
## 집마다 치킨거리를 각각 구할 때 치킨 거리가 짧은 좌표에 cnt +=1 을 해준다
## count 개수에 따라 정렬하고 왼쪽에 뽑음

N,M = map(int,input().split())

Maps = [list(map(int,input().split())) for _ in range(N)]

house = deque()
chicken = deque()

for i in range(N) :
    for j in range(N) :
        if Maps[i][j] == 1 :
            house.append((i+1,j+1))
        elif Maps[i][j] == 2 :
            chicken.append((i+1,j+1))
minimum = 1000000
for i in combinations(chicken,M) :
    res = 0
    Q = deque(i)
    house_copy = copy.deepcopy(house)
    
    while house_copy :
        cnt = 1000000
        x,y = house_copy.popleft()
        for v,w in Q :
            cnt = min(cnt,abs(x-v)+abs(y-w))
        res += cnt
    minimum = min(res,minimum)
    
            
print(minimum)            
