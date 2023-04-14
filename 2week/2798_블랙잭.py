import sys

input = sys.stdin.readline


N,M = map(int,input().split())

N_list = list(map(int,input().split()))


res = 300000
cnt = 300000

for i in range(N) :
    for j in range(i+1,N) :
        for k in range(j+1,N) :
          if M-(N_list[i] + N_list[j] + N_list[k])>= 0 :
              cnt = M-(N_list[i] + N_list[j] + N_list[k])

          res = min(res,cnt)


print(M-res)

