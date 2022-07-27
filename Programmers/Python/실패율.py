def solution(N, stages):
    users = [stages.count(i+1) for i in range(N+1)]
    
    clear = [[i+1, 0] for i in range(N)]
    for i in range(N):
        if sum(users[i:]):
            clear[i][1] = users[i]/sum(users[i:])
        else: 
            clear[i][1] = 0
            
    clear.sort(key=lambda x: x[1], reverse=True)
    return list(map(lambda x: x[0], clear))