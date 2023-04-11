def solution(s):
    li = list(map(int, s.split()))
    return str(min(li)) + " " + str(max(li))

# 공백을 기준으로 문자열을 나누고, 정수형으로 변환한 후 li에 저장
# 최솟값과 최댓값을 구해서 공백과 합쳐서 반환