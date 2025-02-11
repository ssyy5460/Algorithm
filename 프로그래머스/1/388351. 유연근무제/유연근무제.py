def solution(schedules, timelogs, startday):
    answer = 0
    # 출근 희망 시간을 분 단위로 변환
    schedules = [(schedule // 100) * 60 + schedule % 100 for schedule in schedules]
    
    for i in range(len(timelogs)):  # 직원
        cnt = 0
        current_startday = startday 
        
        for j in range(len(timelogs[0])):  # 요일
            if current_startday in (6, 7): # 주말 처리
                current_startday = 1 if current_startday == 7 else current_startday + 1
                continue
    
            log_time = (timelogs[i][j] // 100) * 60 + timelogs[i][j] % 100 # 출근 시간
            
            # 평일: 출근 시간이 희망 시간 + 10분 이내인지 확인
            if log_time <= schedules[i] + 10:
                cnt += 1
            current_startday += 1 

        # 평일 시간 내 출근한 경우
        if cnt == 5:
            answer += 1
    return answer
