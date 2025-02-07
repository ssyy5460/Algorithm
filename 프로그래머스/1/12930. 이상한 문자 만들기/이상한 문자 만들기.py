def solution(s):
    words = s.split(' ')  # 공백을 기준으로 단어를 나눕니다.
    result = []
    
    for word in words:
        new_word = ''
        for i, char in enumerate(word):
            if i % 2 == 0:  # 짝수 인덱스
                new_word += char.upper()  
            else:  # 홀수 인덱스
                new_word += char.lower()  
        result.append(new_word) 
    
    return ' '.join(result)  # 변환된 단어들을 공백으로 연결하여 반환합니다.
