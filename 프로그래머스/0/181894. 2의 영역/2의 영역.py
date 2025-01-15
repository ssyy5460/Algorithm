def solution(arr):
    index = list(filter(lambda x: arr[x] == 2, range(len(arr))))
    
    if len(index) == 0:
        return [-1]
    
    else:   
        return arr[index[0] : index[-1] + 1]