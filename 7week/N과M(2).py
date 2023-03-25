import sys

input = sys.stdin.readline


n,m = map(int, input().split())


result = []
checked = [False] * (n+1)

def recur(number) :
    if number == m :
        print(' '.join(map(str,result)))
        return
    
    

    for i in range(1,n+1) :
        if checked[i] == False :
                checked[i] = True
                result.append(i)
                recur(number+1)
                for j in range(i+1,n+1) :
                    checked[j] = False
                
                result.pop()

                



recur(0)