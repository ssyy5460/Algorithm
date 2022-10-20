from itertools import combinations

def solution(number):

    answer = 0
    com = combinations(number, 3)

    for val in com:
        if sum(val) == 0:
            answer += 1
        else:
            continue

    return answer