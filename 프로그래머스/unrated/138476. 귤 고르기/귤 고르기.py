# from itertools import combinations
from collections import Counter

def solution(k, tangerine):
    ans = 0
    
    for c in Counter(tangerine).most_common():
        k -= c[1]
        ans += 1
        
        if k <= 0:
            return ans
    # 시간초과 코드( test case 정답)
    # ans = [len(set(x)) for x in set(combinations(tangerine, k))]
    # return min(ans)

