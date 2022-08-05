def solution(N, stages):
    answer = {}
    length = len(stages)
    for stage in range(1,N+1):
        if length != 0:
            count = stages.count(stage)
            answer[stage] = count / length
            length -= count
        else:
            answer[stage] = 0
            
            
    return sorted(answer, key = lambda x : answer[x],reverse = True)