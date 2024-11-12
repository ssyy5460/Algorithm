
def can_place_mat(park, x, y, size):
    # 주어진 위치 (x, y)에서 size 크기의 돗자리를 깔 수 있는지 확인
    for i in range(size):
        for j in range(size):
            # park의 경계를 넘어가거나 '-1'이 아닌 경우
            if x + i >= len(park) or y + j >= len(park[0]) or park[x + i][y + j] != '-1':
                return False
    return True

def solution(mats, park):
    # park의 각 위치를 '-1'로 초기화
    for i in range(len(park)):
        print(type(park[i]))
        park[i] = list(park[i])  # 문자열을 리스트로 변환

    # mats를 내림차순으로 정렬하여 가장 큰 돗자리부터 시도
    mats.sort(reverse=True)

    for size in mats:
        for i in range(len(park)):
            for j in range(len(park[0])):
                if can_place_mat(park, i, j, size):
                    return size  # 가장 큰 돗자리 크기 반환

    return -1  # 아무것도 깔 수 없는 경우
