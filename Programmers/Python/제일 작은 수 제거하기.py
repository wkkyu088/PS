def solution(arr):
    arr.remove(min(arr))
    if not arr:
        arr.append(-1)
    return arr

def solution(arr):
    arr.remove(min(arr))
    return arr or [-1]