def solution(n, lost, reserve):
    answer = 0
    dress = [1 for _ in range(n)]
    for l in lost:
        dress[l - 1] -= 1
    for r in reserve:
        dress[r - 1] += 1

    for i in range(len(dress)):
        if dress[i] == 0:
            if dress[i - 1] > 1:
                dress[i - 1] -= 1
                dress[i] += 1
            elif dress[i + 1] > 1:
                dress[i + 1] -= 1
                dress[i] += 1

    for i in dress:
        if i > 0:
            answer += 1
    return answer