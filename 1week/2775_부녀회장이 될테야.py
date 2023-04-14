T = int(input())



for i in range(T) :
    k = int(input())
    n = int(input())

    solution =[]
    for i in range(n) :
        solution.append(i+1)

    
    
    for j in range(k) :
        a=0
        for i in range(n) :
            a += solution[i]
            solution[i] =a

    print(solution[-1]) 
 
 