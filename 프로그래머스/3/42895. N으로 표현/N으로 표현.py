def solution(N, number):
    # 중복 허용 없이 N을 만들 수 있는 조합을 저장할 리스트
    # 5, 55, 555와 같이 반복되는 숫자를 먼저 넣기
    
    combinations = [set([int(str(N)*i)]) for i in range(1,9)]

    # DP를 활용하여 모든 조합을 만들어가며 탐색
    for i in range( 8):
        for j in range(i):
            for op1 in combinations[j]:
                for op2 in combinations[i-j-1]:
                    
                    combinations[i].add(op1 + op2)
                    combinations[i].add(op1 - op2)
                    combinations[i].add(op1 * op2)
                    
                    if op2 != 0:
                        combinations[i].add(op1 // op2)

        if number in combinations[i]:
            return i + 1

    return -1