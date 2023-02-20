from collections import deque

def solution(A, B):
    answer = ''
    result = 0
    if A == B:
        return 0
    
    queue = deque(A)
    ans = deque(B)
    while result <= len(B):
        val = queue.pop()
        queue.insert(0,val)
        print(queue)
        result += 1
        if queue != ans:
            continue
        if queue == ans:
            return result

    return -1
        

