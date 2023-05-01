def solution(begin, target, words):
    stack = [(begin, 0)]
    while stack:
        temp, cnt = stack.pop(0)
        if temp==target:
            return cnt
        for i, w in enumerate(words):
            if sum(i!=j for i, j in zip(temp, w))==1:
                del words[i]
                stack.append((w, cnt+1))
    return 0