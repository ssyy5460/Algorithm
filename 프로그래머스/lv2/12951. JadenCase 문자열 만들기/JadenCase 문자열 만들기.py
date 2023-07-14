def solution(s):
    answer = []
    splited_s = s.lower().split(' ')
    for val in splited_s:
        if val[0].isdigit():
            answer.append(val[0] + val[1:])
        elif val[0].isalpha():
            answer.append(val[0].upper() + val[1:])
    return ' '.join(answer)