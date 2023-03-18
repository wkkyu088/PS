def solution(n, m, section):
    answer = 1
    
    temp = section[0]
    for s in section:
        if s > temp+m-1:
            answer += 1
            temp = s
    
    return answer