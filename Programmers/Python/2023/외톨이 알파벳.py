def solution(str):
    answer = ''
    seperate = []
    cnt = []
    
    temp = [str[0], 0]
    for i in range(1, len(str)):
        if temp[0] != str[i]:
            seperate.append(temp[0])
            cnt.append(i-temp[1])
            temp = [str[i], i]     
    seperate.append(temp[0])
    cnt.append(len(str)-temp[1])

    for i in range(len(seperate)):
        if seperate[i] not in answer and seperate.count(seperate[i]) > 1:
            answer += seperate[i]

    return "".join(sorted(list(answer))) if len(answer) > 0 else "N"


# 글자 종류가 바뀔 때마다 나눔
# 각각을 한 글자 씩 변환, 리스트에 같은 글자가 있다면 외톨이 O