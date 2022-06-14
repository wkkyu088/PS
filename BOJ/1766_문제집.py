import sys, heapq

n, m = map(int, sys.stdin.readline().split())
answer, queue = [], []
graph = [[] for _ in range(n + 1)]
inDegree = [0 for _ in range(n+1)]

# 그래프 만들고 집입 차수 세기
for i in range(m):
    first, second = map(int, sys.stdin.readline().split())
    graph[first].append(second)
    inDegree[second] += 1

# 힙을 이용해 진입차수가 0인 노드를 큐에 채우기
for i in range(1, n + 1):
    if inDegree[i] == 0:
        heapq.heappush(queue, i) 
        
# 쉬운 문제부터 큐에서 꺼내고 차수 1씩 낮추기, 차수 0인 노드 다시 채우기
while queue:
    tmp = heapq.heappop(queue)
    answer.append(tmp)
    for i in graph[tmp]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(queue, i)

print(*answer)