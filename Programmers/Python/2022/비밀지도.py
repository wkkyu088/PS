def solution(n, arr1, arr2):
    answer = []           
    for i in range(n):
        a = bin(arr1[i]|arr2[i])[2:].zfill(n).replace('0', ' ').replace('1', '#')
        answer.append(a)
    return answer