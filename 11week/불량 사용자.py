from collections import defaultdict
import copy

def solution(user_id, banned_id):
    sol = defaultdict(list)
    user = defaultdict(str)

    for i in user_id:
        user[i] = False
    for i in user_id:
        for j in banned_id:
            cnt = 0
            if len(i) == len(j):
                for x in range(len(i)):
                    if i[x] != j[x]:
                        if j[x] != "*":
                            break

                    cnt += 1

            if cnt == len(j):
                if i not in sol[j]:
                    sol[j].append(i)
    res = [0]
    Q = []
    absol = []
    def backtracks(depth,arr):
        if depth == len(banned_id):
            arr.sort()

            if arr not in absol :
                absol.append(arr)
                res[0] += 1       
            return
        for x in sol[banned_id[depth]]:    
            if not user[x] :        
                user[x] = True
                arr.append(x)
                backtracks(depth+1,copy.deepcopy(arr))
                arr.pop()
                user[x] = False
        return

    backtracks(0,Q) 
    return res[0]