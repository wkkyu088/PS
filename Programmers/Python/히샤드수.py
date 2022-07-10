def solution(x):
    return not x%sum(map(int,str(x)))

def solution(x):
    return x%sum([int(i) for i in str(x)]) == 0