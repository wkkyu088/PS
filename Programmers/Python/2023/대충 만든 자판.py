def solution(keymap, targets):
    answer = []
    
    for ts in targets:
        result = 0
        for t in ts:
            temp = 1000
            for k in keymap:
                if k.find(t) != -1:
                    idx = k.find(t)+1
                    if temp > idx:
                        temp = idx
            result += temp
        answer.append(result if result<1000 else -1)
    
    return answer