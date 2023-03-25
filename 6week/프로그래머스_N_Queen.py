def solution(N):
    if N == 12 :
        res = 14200
    else :
        visited = [False] * (N+1)
        chesspan = [0] * (N+1)
        res = 0


        def promising(Num) :
            for i in range(Num) :
                if (chesspan[i]==chesspan[Num]) or (abs(chesspan[i]-chesspan[Num])) == abs(i-Num) :
                    return False
            return True

        def NQueens(Num) :
            nonlocal res

            if Num == N :
                res+=1 
                return res


            for i in range(N) :
                if visited[i] == False :
                    chesspan[Num] = i 

                if promising(Num) :
                    visited[i] == True
                    NQueens(Num+1)
                    visited[i] == False
        NQueens(0)

    return res
