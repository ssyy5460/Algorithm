def solution(n, m, section):
    answer = 0  # 필요한 롤러의 개수
    
    # 롤러로 현재 덮을 수 있는 최대 위치
    max_cover = 0
    
    # 모든 구간을 확인
    for i in range(len(section)):
        # 현재 구간이 롤러로 덮을 수 있는 범위 내에 없다면, 새로운 롤러가 필요
        if section[i] > max_cover:
            answer += 1
            max_cover = section[i] + m - 1  # 새로운 롤러로 덮을 수 있는 최대 범위 업데이트
            
    return answer
