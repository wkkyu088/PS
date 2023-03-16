from heapq import *

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while scoville[0]<K and len(scoville)!=1:
        min1 = heappop(scoville)
        min2 = heappop(scoville)
        heappush(scoville, min1 + min2*2)
        answer += 1
    return -1 if scoville[0]<K else answer