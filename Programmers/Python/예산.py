def solution(d, budget):
    D = sorted(d)
    while sum(D) > budget:
        D.pop()
    return len(D)