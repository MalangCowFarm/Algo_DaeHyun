import sys

input = sys.stdin.readline 

N = list(input().rstrip())

for i in range(len(N)) :
    if N[i].isupper() :
        N[i] = N[i].lower()
    elif N[i].islower() :
        N[i] = N[i].upper()

res = ""

for i in N :
    res += i

print(res)