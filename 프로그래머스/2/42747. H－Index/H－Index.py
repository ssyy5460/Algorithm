def solution(citations):
    
    lst_cit = sorted(citations, reverse = True)

    cnt = 0
    
    for i, val in enumerate(lst_cit):
        if val >= sum(1 for num in lst_cit if num >= val):
            cnt += 1
            
    return cnt if cnt != 0 else max(lst_cit)
