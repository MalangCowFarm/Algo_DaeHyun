import sys

input = sys.stdin.readline


n,m = map(int, input().split())

N_list = sorted(list(set(map(int,input().split()))))

result = []

def recur(number) :
    
    if number == m :
        print(' '.join(map(str,result)))
        return

    for i in N_list :
        if len(result) ==0 or i >= result[-1] :
            
            result.append(i)
            recur(number+1)
            result.pop()


recur(0)
