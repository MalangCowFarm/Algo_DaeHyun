# import sys
# from pprint import pprint
# import copy
# input = sys.stdin.readline

# ## 상어 이동시 -> 백트래킹
# ## 처음 상어 (0,0) 먹기 때문에 0,0은 의미를 가지지않음
# ## ai는 물고기의 번호 , b1는 방향
# # 1 : 위 2: 왼위, 3: 왼 : 4: 왼아래, 5: 아래, 6: 오른아래, 7: 오른 , 8: 오른위
# directions = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
# Maps = [list(map(int,input().split())) for _ in range(4)]


# def backtracks(x,y,copy_maps,dir) :
#     global cnt,maxi
#     pprint(copy_maps)
#     cnt += copy_maps[x][y][0]
#     if not (0<=x+directions[dir][0]<4 and 0<=y+directions[dir][1]<4) :
#         # cnt += Maps[s_x][s_y]
#         if maxi < cnt :
#             maxi = cnt
#         return
    
#     i = 1
#     while i <= 16 :
#         flag = False 
#         for u in range(4) :
#             for y in range(4) :
               
#                 if copy_maps[u][y] and  copy_maps[u][y][0] == i :
#                     v = u
#                     w = y
#                     z = copy_maps[u][y][1]
#                     flag = True 
#                     break
#         if flag :
#             z = z % 8
#             ni = v + directions[z][0]
#             nj = w + directions[z][1]
           
#             while True  :
#                 if (0<= ni <4 and 0<= nj <4) and copy_maps[ni][nj] != 0 and copy_maps[ni][nj][0] != 'x' :
#                     break
#                 z = (z+1) % 8
#                 ni = v + directions[z][0]
#                 nj = w + directions[z][1]
            
#             copy_maps[v][w] = (i,z)
#             copy_maps[v][w],copy_maps[ni][nj] = copy_maps[ni][nj],copy_maps[v][w]

           
#         i+=1

#     for i in range(1,5) :
#         nx = x + directions[dir][0]*i
#         ny = y + directions[dir][1]*i
#         if (0<=nx <4 and 0<= ny <4) and copy_maps[nx][ny] != 0 :
#             backtracks(nx,ny,cnt,copy.deepcopy(copy_maps),copy_maps[nx][ny][1])
        
            



# maxi = cnt = 0
# direct = []
# for i in range(4) :
#     k = 0
#     for j in range(4) :
#         direct.append((Maps[i][k],Maps[i][k+1]-1))
#         Maps[i][j] = (Maps[i][k],Maps[i][k+1]-1)
#         k+=2
#     Maps[i] = Maps[i][:4]

# Maps[0][0] = ('x',Maps[0][0][1])
# s_x = 0; s_y = 0
# direct = sorted(direct)


# backtracks(0,0,Maps,Maps[0][0][1])
# print(maxi)

import copy

board = [[] for _ in range(4)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        # 물고기 번호, 방향
        fish.append([data[2*j], data[2*j+1]-1])
    board[i] = fish


max_score = 0


def dfs(sx, sy, score, board):
    global max_score
    score += board[sx][sy][0]
    max_score = max(max_score, score)
    board[sx][sy][0] = 0

    # 물고기 움직임
    for f in range(1, 17):
        f_x, f_y = -1, -1
        for x in range(4):
            for y in range(4):
                if board[x][y][0] == f:
                    f_x, f_y = x, y
                    break
        if f_x == -1 and f_y == -1:
            continue
        f_d = board[f_x][f_y][1]

        for i in range(8):
            nd = (f_d+i) % 8
            nx = f_x + dx[nd]
            ny = f_y + dy[nd]
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue
            board[f_x][f_y][1] = nd
            board[f_x][f_y], board[nx][ny] = board[nx][ny], board[f_x][f_y]
            break

    # 상어 먹음
    s_d = board[sx][sy][1]
    for i in range(1, 5):
        nx = sx + dx[s_d]*i
        ny = sy + dy[s_d]*i
        if (0<= nx < 4 and 0<= ny < 4) and board[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(board))

dfs(0, 0, 0, board)
print(max_score)