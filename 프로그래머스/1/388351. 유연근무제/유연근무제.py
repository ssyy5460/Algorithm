def solution(schedules, timelogs, startday):
    answer = 0
    
    # 출근 희망 시각을 분 단위로 변환
    for i in range(len(schedules)):
        schedules[i] = (schedules[i] // 100) * 60 + schedules[i] % 100   

    for i in range(len(timelogs)):  # 직원
        cnt = 0
        current_startday = startday 
        
        for j in range(len(timelogs[0])):  # 요일
            timelogs[i][j] = (timelogs[i][j] // 100) * 60 + timelogs[i][j] % 100   

            # 주말 처리
            if current_startday == 6 or current_startday == 7: 
                current_startday += 1
                if current_startday > 7:  
                    current_startday = 1
                continue
            
            # 평일: 출근 시각이 희망 시각 + 10분 이내인지 확인
            if timelogs[i][j] <= schedules[i] + 10:  
                cnt += 1
            
            current_startday += 1 

        
        # 평일 제시간에 출근한 경우
        if cnt >= 5:  
            answer += 1
        
    return answer  
