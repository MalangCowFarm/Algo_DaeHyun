import heapq

import sys

input = sys.stdin.readline 

N = int(input())

heap_p = []
heap_m = []

for i in range(N) :
    num = int(input())
    if num > 0 :
        heapq.heappush(heap_p,-num)

    elif num < 0 :
        heapq.heappush(heap_m,num)
    
    elif num == 0 :
        if heap_p and heap_m :
            if abs(max(heap_p))> abs(min(heap_m)) :
                print(-heapq.heappop(heap_p))

            else :
                print(heapq.heappop(heap_m))
        elif heap_p :
            print(-heapq.heappop(heap_p))
        
        elif heap_m :
            print(heapq.heappop(heap_m))

        elif not heap_p and not heap_m :
            print(0)
            



    # if heap_p and heap_m :
    #     

