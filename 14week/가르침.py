import sys
from itertools import combinations
input = sys.stdin.readline

N,K = map(int,input().split())

#필터링
if K < 5 :
    print(0)
    exit()

chr_Q = []
chr_list = set()
cnt = 0
 
for _ in range(N) :
    chars = input().rstrip()
    fil_c = ''
    for char in chars :
       
        if char not in ['a','n','i','c','t'] :
            fil_c += char

    if len(fil_c) == 0 :
        cnt+=1
    else :
        chr_Q.append(fil_c)
        for x in fil_c :
            chr_list.add(x)

def check(arr) :
    cnt2 = 0
    for x in chr_Q :
        flag = False
        for y in x :
            if y not in arr :
   
                flag = True
                break
        if not flag :
            cnt2+=1

    return cnt2

def dfs() : 
    global cnt
    if len(chr_list) <= K-5 :
       
        cnt += len(chr_Q)
        return
    maxi = 0
    for i in combinations(chr_list,K-5) :
        maxi = max(maxi,check(i))
    cnt += maxi
    return

dfs()
print(cnt)


