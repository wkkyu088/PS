def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    
    while A:
        x, y = A.pop(0), B.pop(-1)
        answer += x*y

    return answer