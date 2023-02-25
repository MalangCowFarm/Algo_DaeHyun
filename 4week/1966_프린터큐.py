import sys

input = sys.stdin.readline

T = int(input())



for i in range(T) :
    N,M = map(int,input().split())
    queue = list(map(int,input().split()))
    
    
    instead_queue = []
    result_instead = []
    
    
    for i in range(N) :
        instead_queue.append(f"{i}")    
    
 
    while True :
        i = 0
        if queue[i] == max(queue) :
            if instead_queue[i] == (f"{M}") :
                result_instead.append(instead_queue[i])
                print(result_instead.index(f"{M}")+1)   
                break
            else :
                
                result_instead.append(instead_queue[i])
                instead_queue.remove(instead_queue[i])
                queue.remove(queue[i])
           

            
        else : 
            instead_queue.append(instead_queue[i])
            instead_queue.remove(instead_queue[i])
            queue.append(queue[i])
            queue.remove(queue[i])