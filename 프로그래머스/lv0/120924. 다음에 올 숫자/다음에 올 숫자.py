def solution(common):
    answer = []
    
    if (common[0]+common[2])/2 == common[1]:
        b = common[1] - common[0]
        answer = common[-1] + b
    # 등비수열
    else: 
        r = common[1] / common[0]
        answer = common[-1] * r
    
    # 등차수열

    return answer
