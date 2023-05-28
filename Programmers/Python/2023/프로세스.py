def solution(pri, location):
    answer = 0
    loc = list(range(len(pri)))
    while pri:
        if pri[0] < max(pri):
            pri = pri[1:] + pri[0:1]
            loc = loc[1:] + loc[0:1]
        else:
            p = pri.pop(0)
            l = loc.pop(0)
            answer += 1
            if location == l:
                return answer