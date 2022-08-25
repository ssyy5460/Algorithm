from collections import deque
def solution(s):
    stack = []
    dq = deque(s)
    ans = True
    while dq:
        val = dq.popleft()
        if val == "(":
            stack.append(val)
        elif val == ')' and stack and stack[-1] == '(':
            stack.pop()
        else:
            ans = False
    return False if stack else ans
