def solution(s):
    answer = []
    loc = {}
    for i in range(len(s)):
        if s[i] not in loc.keys():
            answer.append(-1)
            loc[s[i]] = i
        else:
            answer.append(i-loc[s[i]])
            loc[s[i]] = i
    return answer