import heapq 

def solution(scoville, K):
    cnt = 0
    
    # 정렬
    scoville.sort()
    
    hq = []
    
    for val in scoville:
        heapq.heappush(hq,val)
        
    while hq[0] < K :
        s1 = heapq.heappop(hq)
        s2 = heapq.heappop(hq)
        
        heapq.heappush(hq, s1+s2*2)
        cnt += 1
        
        # 스코빌 지수 만족 못하는 경우
        if len(hq) == 1 and hq[0] < K :
            return -1
        
    return cnt
    
    
    return cnt