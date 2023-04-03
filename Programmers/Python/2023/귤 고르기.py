import collections

def solution(k, tangerine):
    size = collections.Counter(tangerine)
            
    total = 0
    for i, v in enumerate(sorted(size.values(), reverse=True)):
        total += v
        if total >= k: return i+1
