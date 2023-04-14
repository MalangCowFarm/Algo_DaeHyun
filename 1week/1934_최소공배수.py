T = int(input())

##유클리드 공식 사용
def Euclid(a,b) :
    while b>0 :
        a,b = b, a%b
    return a 

for i in range(T) :
    num1, num2 = map(int,input().split())
    print((num1*num2)//(Euclid(num1,num2)))
    