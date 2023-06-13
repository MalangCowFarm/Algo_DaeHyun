def solution(numbers, hand):
    answer = ''
    l = r = (0,3)
    l_lst = [1,4,7]
    r_lst = [3,6,9]
    remain = [2,5,8,0]
    for i in numbers :

        if i in l_lst :
            answer+='L'
            l = (0,l_lst.index(i))
            continue
        if i in r_lst :
            answer+='R'
            r = (0,r_lst.index(i))
            continue
        
        chk = remain.index(i)
        if abs(chk-l[1])-l[0] > abs(chk-r[1])-r[0] :
            answer+="R"
            r = (1,chk)
        elif abs(chk-l[1])-l[0] < abs(chk-r[1])-r[0] :
            answer+="L"
            l = (1,chk)
        else :
            if hand == "right" :
                answer+="R"
                r = (1,chk)
            else :
                answer+="L"
                l = (1,chk)

    return answer