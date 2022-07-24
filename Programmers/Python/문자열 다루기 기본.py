def solution(s):
    return s.isdigit() and len(s) in (4, 6)

def solution(s):  
    return (len(s)==4 or len(s)==6) and s.isdigit()