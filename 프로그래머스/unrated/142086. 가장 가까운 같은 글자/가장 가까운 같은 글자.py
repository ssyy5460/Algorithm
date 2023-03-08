def solution(s):
    check = {}
    result = []
    
    for i, cur in enumerate(s):
        if cur in check:
            result.append(i - check[cur])
            check[cur] = i
            
        else:
            result.append(-1)
            check[cur] = i
            
    return result