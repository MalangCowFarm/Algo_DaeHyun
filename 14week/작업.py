import sys

input = sys.stdin.readline

N = int(input())
second = [0] * (N+1)
adj = {}

for i in range(1,N+1) :
    lst = list(map(int, input().split()))
    second[i] = lst[0]
    if lst[1] == 0 :
        continue
    for j in lst[2:] :
        if i in adj :
            adj[i].append(j)
        else :
            adj[i] = [j]

for i in range(1,N+1) :
    if i in adj :
        seconds = 0
        for j in adj[i] :
            seconds = max(seconds,second[j])
        second[i] += seconds

print(max(second))