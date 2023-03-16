def zipStr(s, n):
    ls = []
    for i in range(0, len(s), n):
        ls.append(s[i:i+n])
    ls.append(' ')
    
    zipped = ""
    cnt = 1
    for i in range(len(ls)-1):
        if ls[i] == ls[i+1]:
            cnt += 1
        else:
            if cnt != 1:
                zipped += str(cnt) + ls[i]
            else:
                zipped += ls[i]
            cnt = 1
    return len(zipped)

def solution(s):
    answer = len(s)
    for i in range(1, len(s)):
        t = zipStr(s, i)
        if t < answer:
            answer = t
    print(answer)
    return answer

solution("aabbaccc")
solution("ababcdcdababcdcd")
solution("abcabcdede")
solution("abcabcabcabcdededededede")
solution("xababcdcdababcdcd")