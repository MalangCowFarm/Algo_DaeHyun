T = int(input())

for i in range(T) :
    H, W, N = map(int,input().split())

    X  = N%H
    Y  = N//H +1
            Y = N//H
            X = H
    print(f'{X*100+Y}')