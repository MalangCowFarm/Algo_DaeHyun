import sys

input = sys.stdin.readline

T = int(input())

sol = []
sign = []
stack = []

for testcase in range(T):
    sol.append(int(input()))

for i in range(sol[0]):
    stack.append(i + 1)
    sign.append("+")

stack.pop()
sign.append("-")

i=0
k=0
while k<=T-2 :
    if sol[i] > sol[i + 1]:
        if stack[-1] != sol[i + 1]:
            print("NO")
            exit()
        else:
            stack.pop()
            sign.append("-")
            sol.remove(sol[i + 1])
    else:
        for t in range(sol[i] + 1, sol[i + 1] + 1):
            stack.append(t)
            sign.append("+")
        stack.pop()
        sign.append("-")
        i+=1
    k+=1

for i in sign :
    print(i)
