import sys
sys.setrecursionlimit(10**6)
def find(parent,x) :
    if parent[x] == x :
        return x
    parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b) :
    rootA = find(parent,a)
    rootB = find(parent,b)

    if rootA < rootB :
        parent[rootB] = rootA

    else :
        parent[rootA] = rootB 



input = sys.stdin.readline

v,e = map(int,input().split())

parent = [0]*(v+1)
edges = []
result = 0 

for i in range(v+1) :
    parent[i] = i

for _ in range(e) :
    check,a,b = map(int,input().split())
    if check == 0 :
        union(parent,a,b)
    else :
        if find(parent,a) == find(parent,b) :
            print('YES')
        else :
            print('NO')