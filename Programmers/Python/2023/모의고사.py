def solution(answers):
    answer = [0,0,0]
    s1 = [1,2,3,4,5]*len(answers)
    s2 = [2,1,2,3,2,4,2,5]*len(answers)
    s3 = [3,3,1,1,2,2,4,4,5,5]*len(answers)
    
    for i, v in enumerate(answers):
        if v==s1[i]: answer[0]+=1
        if v==s2[i]: answer[1]+=1
        if v==s3[i]: answer[2]+=1
    return [i+1 for i, v in enumerate(answer) if v==max(answer)]