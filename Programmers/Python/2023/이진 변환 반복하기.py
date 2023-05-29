def solution(s):
    answer = [0, 0]
    while s != "1":
        cnt = len(s.count("1")*"1")
        answer[0] += 1
        answer[1] += len(s)-cnt
        s = bin(cnt)[2:]
    return answer