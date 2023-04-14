import sys

N,M = map(int,sys.stdin.readline().split())

name = {}
digits = {}
for i in range(1,N+1) :
    Num1 = sys.stdin.readline().strip()
    name[i] = Num1
    digits[Num1] = i


for _ in range(M) :
    Num2 = sys.stdin.readline().strip()
    
    if Num2.isdigit() == True :
        print(name[int(Num2)])
    else :
        print(digits[Num2])
        