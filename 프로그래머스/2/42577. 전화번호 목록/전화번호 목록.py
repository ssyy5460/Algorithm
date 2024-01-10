def solution(phone_book):
    answer = True
    hash_map = {}
    
    # 중복된 번호 체크
    for phone_number in phone_book:
        if phone_number in hash_map:
            return False
        hash_map[phone_number] = 1
    
    # 각 번호의 접두어 체크
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp != phone_number and temp in hash_map:
                return False
    
    return answer