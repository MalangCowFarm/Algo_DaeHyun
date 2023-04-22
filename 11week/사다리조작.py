import sys
input = sys.stdin.readline

N, M ,H = map(int,input().split())
ladder = [[0]*(N+2) for _ in range(H+2)]
solute = 1e9

# i에서 출발해서 i로 도착하는지 탐색하는 함수
def go(x,y,iy):
    while x < H+2:
        if ladder[x][y] == 0:
            x += 1
        else:
            y = ladder[x][y]
            x += 1
    if y == iy:
        return False
    else:
        return True

# 유망한지 판별 => 만약 1~N까지 go함수 진행 중에 하나라도 False가 반환하면 False를 반환하고 끝냄 -> 모두 True라면 마지막에 True 반환
def promising():
    for i in range(1,N+1):
        if go(0,i,i):
            return False
    return True

# 백트래킹 진행 
def back(gets,n):
    global solute
    if n >= solute:return # 현재 최소값보다 많다면 탐색할 필요 없으므로 RETURN
    if promising():# 유망하다면 최소값 갱신
        solute = min(n,solute) 
    if gets> N:return ## 세로선보다 많이 깔면 RETURN
    if n == 3:return ## 3개 초과는 깔 필요가 없으므로 RETURN
    for i in range(1, H + 1):
        if gets<= 1:continue # 가장 위라면 옆에 사다리를 놓을 수 없으므로 한 칸 내려가야 함 그래서 continue 
        if ladder[i][gets] or ladder[i][gets-1]:continue # 양 옆에 사다리가 이미 존재한다면 놓을 수 없으므로 continue 

        ladder[i][gets] = gets-1
        ladder[i][gets-1] = gets
        back(gets,n+1)
        ladder[i][gets] = 0
        ladder[i][gets-1] = 0

    back(gets+1,n)

# 사다리가 있는곳을 번호로 표시해서 번호를 따라 이동할 수 있도록 함
for _ in range(M):
    a, b = map(int,input().split())
    ladder[a][b] = b+1
    ladder[a][b+1] = b 

back(1,0)

if solute < 4:print(solute)

else:print(-1)