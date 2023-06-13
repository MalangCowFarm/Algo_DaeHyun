def solution(A, B):
    A.sort()
    B.sort()
    j = cnt = 0 
    for i in A :
        while j < len(B) :
            if i < B[j] :
                cnt+=1
                j+=1
                break
            else :
                j+=1
        if j == len(B) :
            break
    
    return cnt