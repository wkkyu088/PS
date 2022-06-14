import sys, heapq

N = int(sys.stdin.readline())
op = [int(sys.stdin.readline()) for _ in range(N)]

heap = []
for x in op:
    if x == 0:
        if heap == []: print(0)
        else: print(heapq.heappop(heap)[1]) # 최대 원소 출력 후 삭제
    else:
        heapq.heappush(heap, (-x, x)) # 원소 x를 삽입
