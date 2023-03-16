def solution(dartResult):
    t = []
    idx = 0
    for i in range(1, len(dartResult)):
        if len(t)==2: break
        if dartResult[i].isdigit() and not dartResult[i-1].isdigit():
            t.append(dartResult[idx:i])
            idx = i
    t.append(dartResult[idx:])
    
    bonus = {'S': 1, 'D': 2, 'T': 3} 
    trial = [0, 0, 0, 0]
    for i in range(3):
        if t[i][:2]=='10':
            trial[i+1] = 10**bonus[t[i][2]]
            if len(t[i])==4:
                if t[i][3]=='*':
                    trial[i+1] *= 2
                    trial[i] *= 2
                else:
                    trial[i+1] *= -1  
        else:
            if int(t[i][0]) in range(10):
                trial[i+1] = int(t[i][0])**bonus[t[i][1]]
                if len(t[i])==3:
                    if t[i][2]=='*':
                        trial[i+1] *= 2
                        trial[i] *= 2
                    else:
                        trial[i+1] *= -1
    return sum(trial)