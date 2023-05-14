import sys,heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    res = 1
    N = int(input())
    if N != 1 :
        Maps = list(map(int,input().split()))
        heapq.heapify(Maps)
        while True :
            a = heapq.heappop(Maps)
            b = heapq.heappop(Maps)
            
            res *= a*b
            if res >= 10**9+7 :
                if res % 10**9+7 == 0 :
                    res =1
                else : 
                    res %= 10**9+7
            if not Maps :
                break 
            heapq.heappush(Maps,a*b)
    else :
        M = int(input())
    print(res)