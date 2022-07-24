def solution(s):
    answer = ''
    temp = list(reversed(sorted(s)))
    for i in temp:
        answer += i
    return answer

def solution(s):
    return "".join(sorted(list(s), reverse=True))