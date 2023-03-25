import heapq 


heap = []


for i in range(6) :
    heapq.heappush(heap,i)


heap.remove(5)

print(heap)


heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)
heapq.heappush(heap,-10)
heapq.heappop(heap)
print(heap)