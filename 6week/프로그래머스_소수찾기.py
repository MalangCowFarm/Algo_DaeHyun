from itertools import combinations




def is_prime_number(x) :
    if x <= 1 :
        return False
    for i in range(2,x) :
        if x % i ==0 or x == 1:
            return False
    return True


def solution(numbers):
    sol_list = []
    N_list= list(numbers)
    cnt = 0
    for i in range(1,len(N_list)+1) :

        nPr = combinations(N_list, i)
        Num_list = list(set(nPr))
        for x in Num_list :

            a = ""
            for y in x :
                a +=y
            a = int(a)
            sol_list.append(a)

        sol_list = list(set(sol_list))    

    for t in sol_list :
        if is_prime_number(t) :

            cnt+=1






    return cnt
