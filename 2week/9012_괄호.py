T = int(input())

for _ in range(T):
    stack = [] ## 스택 생성

    VPS_list = list(input())

    for i in VPS_list:
        if i == "(":
            stack.append(i) ## (가 나오면 스택에 요소 추가

        elif i == ")":
            if len(stack) == 0:
                stack.append(i) ## 스택이 비어 있으면 )를 하나 추가하고 반복문 종료
                                ## 밑에 if문에서 No를 출력하기 위해 원소를 넣어주는 것으로, 굳이 i가 아니더라도 아무것이나 스택에 넣고 break하면 된다.
                break
            else:
                stack.pop()

    if len(stack) == 0:
        print("YES")

    else:
        print("NO")