def solution(n):
    answer = ''
    steps = []
    for i in range(1, 20):
        steps.append(3**i)
    
    c = [4, 1, 2]
    answer += str(c[n%3])
    temp = n
    for s in steps:
        if temp <= s: break
        temp = temp - s
        n1 = temp // s
        if temp % s == 0:
            answer += str(c[n1%3])
        else:
            answer += str(c[(n1+1)%3])
    
    return answer[::-1]