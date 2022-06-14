def solution(sizes):
    # 가로가 세로보다 더 크도록 맞추기
    for s in sizes:
        if s[0] < s[1]: 
            s[0], s[1] = s[1], s[0]
    
	# 가로, 세로 각각 최대값 구하기        
    maxW = max([s[0] for s in sizes])
    maxH = max([s[1] for s in sizes])
        
    return maxW*maxH