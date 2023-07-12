def solution(a, b, n):
    total_cnt = 0
    while a <= n:
        total_cnt += (n//a) * b 
        n = (n//a)*b +(n%a)
    return total_cnt

    answer = 0
