def solution(s):
    
    def expand(left, right):
        while left >= 0 and right < len(s)  and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    # 문자열의 길이가 2보다 작거나 문자열이 이미 팰린드롬을 만족했을 경우
    if len(s) < 2 or s == s[::-1]:
        return len(s)
    
    answer = ''
    for i in range(len(s)-1):
        answer = max(answer, expand(i,i+1), expand(i,i+2), key = len)
    return len(answer)