def isPossible(result):
    for r in result:
        x, y, a = r
        if a == 0:
            if y == 0 or [x, y-1, 0] in result or [x-1, y, 1] in result or [x, y, 1] in result:
                continue
            return False
        else:
            if [x, y-1, 0] in result or [x+1, y-1, 0] in result or ([x-1, y, 1] in result and [x+1, y, 1] in result):
                continue
            return False
    return True
        

def solution(n, build_frame):
    answer = []
    
    for x, y, a, op in build_frame:
        item = [x, y, a]
        if op == 1:
            answer.append(item)
            if not isPossible(answer):
                answer.remove(item)
        else:
            answer.remove(item)
            if not isPossible(answer):
                answer.append(item)
                
    answer.sort()
    return answer