## stack = FILO


import sys

input = sys.stdin.readline


while True :
    
    Char_list = list(input().rstrip())
    
    if len(Char_list) == 1 and Char_list[0] == '.' :
        break
    
    
    stack = []

    for i in range(len(Char_list)) :
        if Char_list[i] == "[" :
            stack.append(Char_list[i])
            
        elif Char_list[i] == "]" :
            if stack and stack[-1] == "[" :
                stack.pop()
                
            else : 
                stack.append(Char_list[i])
        
        elif Char_list[i] == "(" :
            stack.append(Char_list[i])
            
        elif Char_list[i] == ")" :
            if stack and stack[-1] == "(" :
                stack.pop()
                
            else : 
                stack.append(Char_list[i])     
        

    if len(stack) == 0 :
            print("yes")
    else :
            print("no")
        