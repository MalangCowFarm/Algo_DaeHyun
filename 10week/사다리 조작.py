import sys
input = sys.stdin.readline

N, M ,H = map(int,input().split())
ladder = [[0]*(N+2) for _ in range(H+2)]
solute = 1e9

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


def promising():
    for i in range(1,N+1):
        if go(0,i,i):
            return False
    return True

def back(gets,n):
    global solute
    if n >= solute:return
    if promising():
        solute = min(n,solute)
    if gets> N:return
    if n == 3:return
    for i in range(1, H + 1):
        if gets<= 1:continue
        if ladder[i][gets] or ladder[i][gets-1]:continue

        ladder[i][gets] = gets-1
        ladder[i][gets-1] = gets
        back(gets,n+1)
        ladder[i][gets] = 0
        ladder[i][gets-1] = 0

    back(gets+1,n)

for _ in range(M):
    a, b = map(int,input().split())
    ladder[a][b] = b+1
    ladder[a][b+1] = b

back(1,0)

if solute < 4:print(solute)

else:print(-1)