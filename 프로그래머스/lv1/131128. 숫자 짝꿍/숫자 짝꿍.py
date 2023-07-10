from collections import Counter
def solution(X, Y):
    answer = ''
    c_X,c_Y = Counter(X), Counter(Y)
    
    # 교집합
    c_XY = c_X & c_Y
    if not c_XY:
        return "-1"
    elif (len(c_XY) == 1) and (c_XY.get('0')) :
        return "0"
    
    for key, value in c_XY.items():
        answer += value * key

    return "".join(sorted(answer, reverse = True))
        
            
    