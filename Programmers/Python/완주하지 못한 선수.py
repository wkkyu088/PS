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

def solution(participant, completion):
    arr = {}
    for p in participant:
        if p in arr: arr[p] += 1
        else: arr[p] = 1
    for c in completion:
        arr[c] += 1
    return [i for i in arr.keys() if arr[i]%2!=0][0]