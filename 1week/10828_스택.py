import sys

input = sys.stdin.readline

N = int(input().strip())

stacks = []


def push(n) :
    stacks.append(n)
    return

def pop(array) :
    if array == [] :
        return print(-1)
    else :
        
        return print(array.pop())
        
def size(array) :
    return print(len(array))

def empty(array) :
    if array == [] :
        return print(1)
    else :
        return print(0)

def top(array) :
    if array == [] :
        return print(-1)
    else :
        return print(array[-1])


for _ in range(N) :
    M = input().strip()
    
    if "push" in M :
        S,I = M.split()
        I = int(I)
        push(I)
    elif M == "pop" :
        pop(stacks)
    elif M == "size" :
        size(stacks)
    elif M == "empty" :
        empty(stacks)
    elif M == "top" :
        top(stacks)
