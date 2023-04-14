import sys

input = sys.stdin.readline 

N_list = list(input().rstrip())

Target = list(input().rstrip())

N_length = len(N_list)
T_length = len(Target)


stack = []

end_char = Target[-1]

for i in N_list :
    stack.append(i)
    if i == end_char and "".join(stack[-T_length:]) == "".join(Target) :
        for i in range(T_length) :
            stack.pop()

    
if not stack :
    print("FRULA")

else :
    print("".join(stack))

    