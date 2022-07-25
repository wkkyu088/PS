def solution(arr):
    temp = arr[0]
    answer = [temp]
    for i in range(1, len(arr)):
        if arr[i] != temp:
            temp = arr[i]
            answer.append(temp)
    return answer

def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != answer[-1]:
            answer.append(arr[i])
    return answer