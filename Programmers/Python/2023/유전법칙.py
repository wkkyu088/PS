def solution(queries):
    Rr = ["RR", "Rr", "Rr", "rr"]
    
    answer = []
    for i in range(len(queries)):
        temp = queries[i][1]
        beans = [temp]
        for j in range(1, queries[i][0]):
            beans.insert(0, (temp-1)//4+1)
    
        pp = "Rr"
        for k in range(1, len(beans)):
            if pp == "Rr":
                pp = Rr[(beans[k]-1)%4]
                
        answer.append(pp)
    return answer

# RR -> [RR, RR, RR, RR]
# Rr -> [RR, Rr, Rr, rr]
# rr -> [rr, rr, rr, rr]

# 부모의 순서 P를 찾는 법
# 3세대; (0,1,2,3) = 0, (4,5,6,7) = 1, (8,9,10,11) = 2, (12,13,14,15) = 3
# => (p-1)//4 = P-1
# () 안에서의 순서는 => (p-1)%4