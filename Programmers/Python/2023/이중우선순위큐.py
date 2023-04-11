def solution(ops):
    queue = []
    for i, v in enumerate(ops):
        op = v.split()
        if op[0] == "I":
            queue.append(int(op[1]))
        elif queue:
            if op[1] == "1":
                queue.remove(max(queue))
            else:
                queue.remove(min(queue))
    return [max(queue), min(queue)] if queue else [0,0]

# 각 명령어에 따라 I라면 큐에 추가하고, D라면 각 명령 수행
# 큐가 비었으면 [0,0], 아니라면 [최댓값, 최솟값] 반환