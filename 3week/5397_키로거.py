import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    stack = []
    temporary = []
    Char_list = input().rstrip()

    for i in Char_list:

        if i.isalpha() or i.isdigit():
            stack.append(i)

        elif i == "<":
            if stack:
                temporary.append(stack.pop())
        elif i == ">":
            if temporary:
                stack.append(temporary[-1])
                temporary.pop()
        elif i == "-":
            if stack:
                stack.pop()
    if temporary:
        for i in reversed(range(len(temporary))):
            stack.append(temporary[i])
    print("".join(stack))