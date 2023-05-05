import sys
input = sys.stdin.readline

rotate = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], [12], [13], [14], [15], [16, 27], [17], [18], [19], [20], [32], [22], [23], [24], [30], [26], [24], [28], [29], [24], [31], [20], [32]]
score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]
dice = list(map(int, input().split()))
res = 0
horse = [0,0,0,0]
gets = []
def backtracking(index, result, horse, gets):
    global res
    if index >= 10:
        if result > res :
            res = result
        return
    for i in range(4):
        x = horse[i]
        if len(rotate[x]) == 2:
            x = rotate[x][1]
        else:
            x = rotate[x][0]
        for j in range(1, dice[index]):
            x = rotate[x][0]
        if x == 32 or (x < 32 and x not in horse):
            r = horse[i]
            horse[i] = x
            gets.append(x)
            backtracking(index + 1, result+score[x],horse, gets)
            gets.pop()
            horse[i] = r


            
backtracking(0, 0, horse, gets)


print(res)