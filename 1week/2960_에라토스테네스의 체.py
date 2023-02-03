N,K = map(int,input().split())

solution = []
real_solution = []
for i in range(2,N+1) :
    solution.append(i)
    



while len(solution) != 0 :
    minimums = min(solution)
    temp = minimums
    ms = temp
    i = 2 
    while ms <= solution[-1] :
        try:
            if ms in real_solution :
                pass
            else :
                real_solution.append(ms)
            solution.remove(ms)
        
        except :
            pass
        if len(solution) == 0 :
            break
      
        ms = minimums*i
      
        i+=1 
        


print(real_solution[K-1])