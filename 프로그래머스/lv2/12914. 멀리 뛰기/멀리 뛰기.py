def solution(n):
    val1, val2 = 1,2
    for i in range(n-1):
        val1,val2 = val2, val1+val2
    return val1 % 1234567