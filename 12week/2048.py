import sys
input = sys.stdin.readline
import sys,copy

input = sys.stdin.readline

N = int(input())

Maps = [list(map(int,input().split())) for _ in range(N)]

def rotate(arr) :
    new =[[0]*N for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
        
            new[j][N-i-1] = arr[i][j]
    return new

def rotate_reverse(arr) :
    new = [[0]*N for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
          
            new[N-j-1][i] = arr[i][j]
    return new

#왼쪽 오른쪽 한번씩 탐색하면 된다

def move_left(arr) :
    for i in range(N) :
        for j in range(N) :
            if arr[i][j] != 0 :
                k = j 
                while 0<=k-1 and arr[i][k-1] == 0 :
                    k-=1 
                
                arr[i][j],arr[i][k] = arr[i][k],arr[i][j]
       
        for y in range(N-1) :
            if arr[i][y] == arr[i][y+1] :
                arr[i][y] = arr[i][y]*2
                arr[i][y+1] = 0
        for y in range(N) :
            k = y 
            while 0<=k-1 and arr[i][k-1] == 0 :
                k-=1
            arr[i][k],arr[i][y] = arr[i][y],arr[i][k] 

    return arr
            
def arr_list(arr) :
    arr_lists = []
    arr_lists.append(rotate_reverse(move_left(rotate(copy.deepcopy(arr)))))
    arr_lists.append(rotate(move_left(rotate_reverse(copy.deepcopy(arr)))))
    arr_lists.append(move_left(copy.deepcopy(arr)))
    arr_lists.append(move_right(copy.deepcopy(arr)))
    
    return arr_lists    
    
def move_right(arr) :
    for i in range(N) :
        for j in range(N-1,-1,-1) :
            if arr[i][j] != 0 :
                k = j 
                while k+1<N and arr[i][k+1] == 0 :
                    k+=1 
                
                arr[i][j],arr[i][k] = arr[i][k],arr[i][j]
       
        for y in range(N-1,0,-1) :
            
            if arr[i][y] == arr[i][y-1] :
                arr[i][y] = arr[i][y-1]*2
                arr[i][y-1] = 0
        for y in range(N-1,0,-1) :
            k = y 
            while k+1<N and arr[i][k+1] == 0 :
                k+=1
            arr[i][k],arr[i][y] = arr[i][y],arr[i][k] 
    return arr
            
def backtracks(arr,depth) :
    global maxi
    if depth == 5 : 
        for i in range(N) :
            for j in range(N) :
                if arr[i][j] > maxi :
                    maxi = arr[i][j]
        return
    for t in arr_list(arr) :
        backtracks(t,depth+1)
        
maxi = 2
backtracks(Maps,0)

print(maxi)