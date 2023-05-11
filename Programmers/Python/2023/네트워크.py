def solution(n, computers):
    answer = 0
    visited = list(range(n))
    
    while visited:
        v = visited.pop(0)
        stack = [(v, computers[v])]
        while stack:
            t, temp = stack.pop(0)
            for i, c in enumerate(temp):
                if i in visited and i!=t and c==1:
                    stack.append((i, computers[i]))
                    visited.remove(i)
        answer += 1
    
    return answer