def solution(number,k):
    stack = []
    
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
            
        stack.append(num)
    
    if k > 0: # k가 0보다 크다면
        stack = stack[:-k]

    return ''.join(stack)