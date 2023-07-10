def solution(name, yearning, photo):
    answer = []
    
    
    for peoples in photo:
        yearning_score = 0
        for people in peoples:
            if people in name:
                yearning_score += yearning[name.index(people)]
        answer.append(yearning_score)
    return answer