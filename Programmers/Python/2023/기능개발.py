def solution(progresses, speeds):
    answer = [0]
    days = []
    for i, v in enumerate(progresses):
        if (100-v)%speeds[i]:
            days.append((100-v)//speeds[i]+1)
        else:
            days.append((100-v)//speeds[i])
            
    temp = days[0]
    for d in days:
        if d > temp:
            answer.append(1)
            temp = d
        else:
            answer[-1] += 1
        
    return answer