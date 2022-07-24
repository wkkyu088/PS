def solution(s):
    cntP = 0
    cntY = 0
    for i in s:
        if i in ('P', 'p'): cntP += 1
        if i in ('Y', 'y'): cntY += 1
    return cntP==cntY

def solution(s):
    return s.upper().count('P') == s.upper().count('Y')