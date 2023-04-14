import sys

input = sys.stdin.readline

N = int(input())

graph_list = [list(map(int,input().split())) for _ in range(N)]

visited = [False for _ in range(N)]


result = 100000000000


def BackTracks(depth, index) :
    if depth == N//2 :
        global result
        Team_one = 0
        Team_two = 0

        for i in range(N) :
            for j in range(N) :
                if visited[i] and visited[j] :
                    Team_one += graph_list[i][j]

                elif not visited[i] and not visited[j] :
                    Team_two += graph_list[j][i]

                
        result = min(result,abs(Team_one-Team_two))
        return
    
    for i in range(index,N) :
        if not visited[i] :
            visited[i] =True
            BackTracks(depth+1,i+1)
            visited[i] = False



BackTracks(0,0)

print(result)