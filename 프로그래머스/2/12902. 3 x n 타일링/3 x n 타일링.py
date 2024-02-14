def solution(n):
    answer = 0
    
    l = [0] * (n+1)
    
    l[2] = 3
    l[4] = 11
    
    for i in range(6, n+1, 2):
        l[i] = 3 * l[i-2] + 2 
    
    return l[n]

