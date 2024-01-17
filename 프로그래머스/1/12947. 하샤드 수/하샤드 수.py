def solution(x):
    sum_x = sum(map(int,str(x)))

    return True if  x % sum_x == 0 else False