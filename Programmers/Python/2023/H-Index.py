def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)
    
    for i in range(len(citations), 0, -1):
        if len([x for x in citations if x>=i]) >= i:
            answer = i
            break
    
    return answer