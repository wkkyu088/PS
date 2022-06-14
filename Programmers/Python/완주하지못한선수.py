def solution(participant, completion):
    answer = ''

    mergeList = []
    mergeList.extend(participant)
    mergeList.extend(completion)

    haspMap = {}
    for i in mergeList:
        if i in haspMap:
            haspMap[i] += 1
        else:
            haspMap[i] = 1

    for i in haspMap.keys():
        if haspMap[i] % 2 != 0:
            answer = i

    return answer