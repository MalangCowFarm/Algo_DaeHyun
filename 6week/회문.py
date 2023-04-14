import sys

input = sys.stdin.readline

N = int(input())

result = 0


def calculate(array) :
    global cnt
    cnt =0
    
    end = len(array) - 1
    start = 0
    while start != end:
        if abs(start - end) == 1:
            if array[start] == array[end]:
                cnt = 1
                break
            else:
                cnt = 2
                break
        if array[start] == array[end]:
            start += 1
            end -= 1

        else:
            cnt = 2
            break
        if start==end :
            cnt =1
            break
    
    return cnt



for x in range(N):
    flag = False
    N_list = list(input().rstrip())
    end = len(N_list) - 1
    start = 0
    while start != end:

        if abs(start - end) == 1:
            if N_list[start] == N_list[end]:
                print(0)
                flag = True
                break
            else:
                print(1)
                flag = True
                break
        if N_list[start] == N_list[end]:
            start += 1
            end -= 1

        else:
            res1 = N_list[start+1:end+1]
            res2 = N_list[start:end]
            break
        if start == end :
            print(0)
            flag =True
            break

    res = 0
    if not flag :
        calculate(res1)
        if cnt == 1 :
            print(1)
            res+=1
            continue
        calculate(res2)
        if cnt == 1 :
            print(1)
            res+=1
        if res == 0 :
            print(2)
        
    
        