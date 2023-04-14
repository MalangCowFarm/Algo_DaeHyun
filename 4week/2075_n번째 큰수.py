import sys 
from queue import PriorityQueue
import heapq

input = sys.stdin.readline


T = int(input().strip())

# queue = PriorityQueue(maxsize=T)
queue = []


for _ in range(T) :
    N = list(map(int,input().strip().split()))
    
    for n in N :
        if len(queue) < T :
            heapq.heappush(queue,n)
        
        else :
            if queue[0] < n :
                heapq.heappop(queue)
                heapq.heappush(queue,n)
                

print(queue[0])