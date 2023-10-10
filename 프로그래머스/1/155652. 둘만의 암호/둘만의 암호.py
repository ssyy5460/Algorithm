def solution(s, skip, index):
    answer = ''
    
    valid_alpha = [chr(x) for x in range(97, 123) if chr(x) not in skip]

    for v in s:
        if v in valid_alpha:
            idx = (valid_alpha.index(v) + index) % len(valid_alpha)
            answer += valid_alpha[idx]
    
    return answer