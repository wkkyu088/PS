def solution(progresses, speeds):
    done = []
    for i, j in zip(progresses, speeds):
        t = (100-i)//j if (100-i)%j==0 else (100-i)//j+1
        done.append(t)
        
    answer = []
    flag = done[0]
    cnt = 1
    for i in range(1, len(done)):
        print(flag, done[i], cnt)
        if done[i] <= flag:
            cnt += 1    
        else:
            answer.append(cnt)
            cnt = 1
            flag = done[i]
    answer.append(cnt)
    return answer