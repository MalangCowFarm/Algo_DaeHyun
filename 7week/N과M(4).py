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
        if checked[i] == False and len(result)==0 or i >= result[-1] :
                checked[i] = True
                result.append(i)
                
                recur(number+1)
      
                    
                checked[i] = False  
                result.pop()

                



recur(0)