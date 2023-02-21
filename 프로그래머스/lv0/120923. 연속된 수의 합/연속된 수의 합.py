def solution(num, total):
    avg = total // num
    return [val for val in range(avg - (num-1)//2,avg+(num+2)//2)]