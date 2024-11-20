def solution(arr):
    answer = 0
    
    cur_arr = arr[:]
    
    while True:
        next_arr = []
        
        for val in cur_arr:
            if val >= 50 and val % 2 == 0:
                next_arr.append(val // 2)  
            elif val < 50 and val % 2 == 1:
                next_arr.append(val * 2 + 1)  
            else:
                next_arr.append(val)  
                
                
        if next_arr == cur_arr:
            break
            
        cur_arr = next_arr
        answer += 1
        
    return answer
        