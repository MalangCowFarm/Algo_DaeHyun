from collections import deque
def solution(people, limit):
    
    people.sort()
    people = deque(people)
    cnt = 0
    while people  :
        total = people[-1]
        while people and total + people[0] <= limit  :
            total += people[0]
            people.popleft()
            
        cnt+=1
        if people :
            people.pop()
    
    return cnt 