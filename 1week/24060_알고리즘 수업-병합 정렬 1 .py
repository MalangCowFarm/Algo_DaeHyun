import sys

solution = []

def merge_sort(arr):
    
    if len(arr) < 2:
        return arr
    if len(arr) % 2 == 0 :
        mid = len(arr) // 2
    elif len(arr) % 2 == 1 :
        mid = len(arr) // 2   + 1

    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            
            l += 1
        else:
            merged_arr.append(high_arr[h])
           
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    for i in range(len(merged_arr)) :
        solution.append(merged_arr[i])
    return merged_arr

A,B = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))


merge_sort(arr)

if len(solution) < B :
    print(-1)
else :
    print(solution[B-1])

