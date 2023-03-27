def solution(genres, plays):
    answer = []
    total = {}
    cnt = {}
    for i, v in enumerate(genres):
        if v not in total.keys():
            total[v] = plays[i]
            cnt[v] = [(plays[i], i)]
        else:
            total[v] += plays[i]
            cnt[v].append((plays[i], i))
    
    sorted_total = list(sorted(total.items(), key=lambda x: -x[1]))
    for i, v in enumerate(sorted_total):
        t = list(sorted(cnt[v[0]], key=lambda x: (-x[0], x[1])))
        if len(t)==1:
            answer.append(t[0][1])
        else:
            answer.append(t[0][1])
            answer.append(t[1][1])
    
    return answer