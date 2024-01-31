def solution(sequence, k):
    answer = []
    prefix_sum = [0] * (len(sequence) + 1)

    for i in range(1, len(sequence) + 1):
        prefix_sum[i] = prefix_sum[i-1] + sequence[i-1]

    start = 0
    end = 0

    while start < len(sequence):
        if end + 1 < len(prefix_sum) and prefix_sum[end+1] - prefix_sum[start] == k: 
            answer.append([start, end])
            start += 1
        elif end + 1 < len(prefix_sum) and prefix_sum[end+1] - prefix_sum[start] < k: 
            end += 1
        else:
            start += 1


    min_length = min(answer, key=lambda x: x[1] - x[0])
    return min_length
