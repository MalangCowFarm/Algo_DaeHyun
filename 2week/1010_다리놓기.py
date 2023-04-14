import sys

input = sys.stdin.readline

def calculator(num1,num2) : ## nCr(조합)을 수행하는 함수 생성
    res = 1
    while num2 != 0 :
        res *= num1
        num1 -=1
        num2 -=1
    return res

T= int(input())

for _ in range(T) :
    N,M = map(int,input().split())

    if N == M :
        print(1)
    else :
        print(calculator(M,N) // calculator(N,N)) # 조합 과정 수행