import sys

input = sys.stdin.readline


n,m = map(int, input().split())

N_list = sorted(list(map(int,input().split())))

result = []
checked = [False] * (n)

def recur(number) :
    
    if number == m :
        
        print(*result)
        return
    cnt = 0
    for i in range(n) :
        if not checked[i] and cnt != N_list[i] :
            checked[i] = True
            result.append(N_list[i])
            cnt = N_list[i]
            recur(number+1)
            checked[i] = False
            result.pop()
            


recur(0)
