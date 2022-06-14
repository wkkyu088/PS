import sys
import heapq

N = int(sys.stdin.readline())
leftHeap = []       # 중간값보다 작은 수 (중간값 포함)
rightHeap = []      # 중간값보다 큰 수
answer = []         # 중간값 배열

for i in range(N):
    n = int(sys.stdin.readline())
    
    # 두 힙의 크기가 같으면 left에 넣고 아니면 right에 넣음
    # left는 최대힙, right는 최소힙
    if len(leftHeap)==len(rightHeap):
        heapq.heappush(leftHeap, (-n, n))
    else:
        heapq.heappush(rightHeap, (n, n))
        
    # left의 루트가 right의 루트보다 크다면 swap
    if rightHeap and leftHeap[0][1] > rightHeap[0][0]:
        min = heapq.heappop(rightHeap)[0]
        max = heapq.heappop(leftHeap)[1]
        heapq.heappush(leftHeap, (-min, min))
        heapq.heappush(rightHeap, (max, max))
    
    # left의 루트는 중간값
    answer.append(leftHeap[0][1])
    
for a in answer: print(a)