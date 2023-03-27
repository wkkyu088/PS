def solution(s):
    stack = []
    for i, v in enumerate(s):
        if v==")" and not stack: return False
        if v=="(": stack.append(v)
        else: stack.pop()
    return False if stack else True