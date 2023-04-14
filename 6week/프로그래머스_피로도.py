def solution(k, dungeons):
    return dungeons_count(k,dungeons,0)

def dungeons_count(k,N_list,cnt):
    
    cnt_list=[cnt]
    for i in range(len(N_list)):
        if N_list[i][0]<=k:
            N_copy_list=N_list.copy()
            del N_copy_list[i]
            cnt_list.append(dungeons_count(k-N_list[i][1],N_copy_list,cnt+1))
    
    return max(cnt_list)