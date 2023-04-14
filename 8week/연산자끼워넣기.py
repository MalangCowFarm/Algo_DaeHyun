import sys

input = sys.stdin.readline 


def calculation(sign,a,b) :
    if sign == "+" :
        return a+b
    elif sign == "-" :
        return a-b
    elif sign == "*" :
        return a*b
    elif sign == "/" :
        if a <0 and b>0:
            return -(-a//b)
        else :
            return a//b


def backtracks(i,res) :
    global maxi,mini
    if len(res) == len(real_op) :
        result = N_list[0]
        for i in range(len(res)) :
            result = calculation(res[i],result,N_list[i+1])
        if result > maxi :
            maxi = result
        if result < mini :
            mini = result
        return
    
    for i in range(len(real_op)) :
        if not visited[i] :
            visited[i] = True
            res.append(real_op[i])
            backtracks(i+1,res)
            visited[i] = False
            res.pop()


N = int(input())

N_list = list(map(int,input().split()))

pmsm = ["+","-","*","/"]
operator = list(map(int,input().split()))

real_op = []
for i in range(4) :
    if operator[i] >=1 :
        while operator[i] > 0 :
            real_op.append(pmsm[i])
            operator[i] -=1
visited = [False]*len(real_op)


res = []
# 함수
maxi = -10**10
mini = 10**10
backtracks(0,res)

print(maxi)
print(mini)

##2번풀이
# import sys


# input = sys.stdin.readline

# N = int(input())

# N_list = list(map(int,input().split()))

# calc_count =list(map(int,input().split()))

# calc_name = ['+','-','*','/']


# mins  = -1000000000
# maxs = 100000000

# def calculator(first,sign,last) :
#     if calc_name[sign] == "+" :
#         result = first + last
       
     
#     elif calc_name[sign] == "-" :
#         result = first - last
       
    
#     elif calc_name[sign] == "*" :
#         result = first*last 
      
    
#     elif calc_name[sign] == "/" :
#         if first < 0 and last > 0 :
#             result = -1*((-1*first)//last)
#         else :
#             result = first//last
#     return result
        
# def calculate(index, result) :
#     global mins,maxs
#     if index == N-1 :
#         mins= max(mins,result)
#         maxs = min(maxs,result)
#         return mins,maxs
#     #백트래킹
#     for i in range(4) :
#         if calc_count[i] >= 1 :
#             calc_count[i] -=1
#             calculate(index+1, calculator(result,i,N_list[index+1]))
#             calc_count[i] +=1
    
            
# calculate(0,N_list[0])

# print(mins)
# print(maxs)