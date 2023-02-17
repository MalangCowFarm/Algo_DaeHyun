import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


K,N = map(int,input().split())

K_list = [input().rstrip() for _ in range(K)]
maxi = 0
for i in K_list :
    maxi = max(int(i),maxi)

def binarySearch(start,end) :
    cnt = 0
    if start == end or abs(start-end) == 1 :
        for i in K_list :
            cnt += int(i)//end
        if cnt == N :
            print(end)
        else :
            print(start)
        return
    mid = (start+end)//2

    for i in K_list :
        cnt += int(i)//mid
    if cnt < N :
        binarySearch(start,mid)
    elif cnt>=N :
        binarySearch(mid,end)

binarySearch(0,maxi)

