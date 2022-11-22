def solution(food):
    answer = ''
    for i,val in enumerate(food):
        if (i > 0) and (val % 2 != 0):
            val -= 1
            val /= 2
            answer += str(i) * int(val)
            
        elif (i > 0) and (val % 2 == 0):
            val /= 2
            answer += str(i) * int(val)
            
    return answer + '0' + answer[::-1]