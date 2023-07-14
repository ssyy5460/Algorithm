def solution(s):
    answer = []
    splited_s = s.split(' ')
    for val in splited_s:
        answer.append(val.capitalize())
    return ' '.join(answer)