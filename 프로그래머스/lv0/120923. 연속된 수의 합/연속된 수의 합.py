def solution(num, total):
    if num % 2 == 0:
        return list(range(total//num-num//2+1, total//num+num//2+1))
    else:
        return list(range(total//num - num//2 , total//num+num//2 + 1))