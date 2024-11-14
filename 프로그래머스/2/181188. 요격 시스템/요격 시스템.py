def solution(targets):
    answer = 0
    targets_sorted = sorted(targets, key=lambda x: (x[0], x[1]))
    return targets_sorted