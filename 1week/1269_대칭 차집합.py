import sys

A,B = map(int,sys.stdin.readline().split())

## 대칭 차집합
## 원소의 개수가 중복될 수 있나?

dict_1 = {}


A_list = list(map(int,sys.stdin.readline().split()))
B_list = list(map(int,sys.stdin.readline().split()))

for i in range(len(A_list)) :
    dict_1[A_list[i]] = 1
    

    
cnt = 0 
for i in range(len(B_list)) :
    if B_list[i] in dict_1.keys() :
        dict_1[B_list[i]] -= 1
    else :
        cnt+=1 
 
for key, value in dict_1.items() :
    if value == 1 :
        cnt+=1

print(cnt)