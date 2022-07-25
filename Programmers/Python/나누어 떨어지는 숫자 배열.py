def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor == 0:
            answer.append(i)
    answer.sort()
    
    return answer or [-1]

def solution(arr, divisor):
    array = list(filter(lambda x: x%divisor==0, arr))
    return sorted(array) or [-1]