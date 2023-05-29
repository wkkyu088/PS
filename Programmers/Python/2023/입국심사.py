'''
# 입국심사
n명이 입국심사를 위해 줄을 서서 기다리고 있습니다. 
각 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간은 다릅니다.

처음에 모든 심사대는 비어있습니다. 
한 심사대에서는 동시에 한 명만 심사를 할 수 있습니다. 
가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있습니다. 
하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있습니다.

모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.

입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 
주어질 때, 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.
'''

def solution(n, times):
    answer = 0
    # right는 가장 비효율적으로 심사했을 때 걸리는 시간
    # 가장 긴 심사시간이 소요되는 심사관에게 n 명 모두 심사받는 경우이다.
    left, right = 1, max(times) * n
    while left <= right:
        mid = (left+ right) // 2
        people = 0
        for time in times:
            # people 은 모든 심사관들이 mid분 동안 심사한 사람의 수
            people += mid // time
            # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수 있다면 반복문을 나간다.
            if people >= n:
                break
        
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우
        if people >= n:
            answer = mid
            right = mid - 1
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 적은 경우
        elif people < n:
            left = mid + 1
            
    return answer

# 내 코드, 테케 2개만 맞고 나머지는 틀림
def solution2(n, times):
    answer = 0
    waits = times[:]
    n = n - len(times)
    idx = 0
    
    while n:
        t = min(waits)
        answer += t
        waits = list(map(lambda x: x-t, waits))
        ls = waits[:]
        for j, v in enumerate(times):
            ls[j] += v
        idx = ls.index(min(ls))
        waits[idx] += times[idx]
        n -= 1
    answer += waits[idx]
    return answer