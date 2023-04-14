def solution(n):
    ans = 0
    while n > 0:
        ans += n % 10
        n //= 10
    return ans

example = []

for i in range(1, 10000):
    example.append(i)

for j in range(10000):
    t = str(j)
    s = list(t)
    if len(s) == 1:
        price = 9
    elif len(s) == 2:
        price = 18
    elif len(s) == 3:
        price = 27
    else:
        price = 36
    for t in range(1, price + 1):
        init = j - t
        maxi = init + solution(init)
        if maxi == j:
            if j in example:
                example.remove(j)


    j += 1

for i in example:
    print(i)
