def recurssive(s, answer):
    if len(s)<1:
        return answer
    same, diff = 1, 0
    x = s[0]
    for i in range(1, len(s)):
        if x==s[i]:
            same += 1
        else:
            diff += 1
        if same==diff:
            answer += 1
            s = s[i+1:]
            print(s)
            recurssive(s, answer)

def solution(s):
    return recurssive(s, 0)
            
            
solution("banana")
# print()
# solution("abracadabra")
# print()
# solution("aaabbaccccabba")