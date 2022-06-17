def solution(numbers):
    answer = []
    # 차례로 두 수를 뽑음
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
            
    # 셋으로 중복 제거, 정렬하여 반환
    return sorted(list(set(answer)))