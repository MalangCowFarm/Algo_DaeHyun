import heapq
import sys

input = sys.stdin.readline

sol = []

N = int(input())

for i in range(N) :
    x = int(input())
    if x % 1 == 0 and x != 0 :
        heapq.heappush(sol,-x)
    elif x == 0 :
        if sol == [] :
            print(0)
        else :
            print(-(heapq.heappop(sol)))