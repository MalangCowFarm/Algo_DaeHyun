import sys

input = sys.stdin.readline

def lis(arr,n) :
    rst = [1] *(n)
    for i in range(1,n) :
        for j in range(i) :
            if arr[j] < arr[i] :
                rst[i] = max(rst[i],rst[j]+1)
    return rst

N = int(input())

Q = []
for _ in range(N) :
    start,end = map(int,input().split())
    Q.append((start,end))

Q.sort()
l = []
for a,b, in Q :
    l.append(b)

print(N-max(lis(l,N)))
