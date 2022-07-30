def solution(lottos, win_nums):
    x = 6-len(set(win_nums)-set(lottos)) # 맞힌 수
    y = lottos.count(0) # 맞힐 수 있는 수
    if x==0 and y==0: return [6, 6]
    return [7-(x+y), 7-x if x!=0 else 6]