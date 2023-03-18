import sys

input = sys.stdin.readline

T = int(input())

sol = []
cnt = []
for _ in range(T) :
    A,B = map(int,input().split())
    sol.append((A,B))

for i in range(T):
    cnt = 0
    for j in range(T):
        if sol[i][0] < sol[j][0] and sol[i][1] < sol[j][1]:
            cnt += 1
    cnt.append(cnt + 1)
    ### 자신보다 키와 몸무게가 모두 큰 사람은 자신보다 등수가 높다는 뜻이므로
    ### 이 등수만 체크해준다면 현재 내 순위를 알 수 있다.
    ##  최소 순위는 1이므로 append시 1을 더해서 append 해주게 된다.

for grade in cnt:
    print(grade, end=" ")