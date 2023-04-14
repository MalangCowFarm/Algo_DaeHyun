import sys

input = sys.stdin.readline


N = int(input())


i = 2
while N>1 :

    if N == 1:
        print("")
    
    if N % i == 0 :
        print(i)
        N = N//i
        i = 2
    else :
        i +=1  

