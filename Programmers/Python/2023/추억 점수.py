def solution(name, yearning, photo):
    answer = [0]*len(photo)
    
    score = dict(zip(name, yearning))
    
    for i, p in enumerate(photo):
        for j, v in enumerate(p):
            try:
                answer[i] += score[v]
            except KeyError:
                answer[i] += 0
        
    return answer

# 추억점수를 딕셔너리로 변경, photo 배열을 순회하면서 추억점수가 있으면 더하고 없으면 0을 더함