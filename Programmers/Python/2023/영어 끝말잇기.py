def solution(n, words):
    answer = [0,0]
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            return [i%n+1, i//n+1]
    return answer

# 첫번째로 끝말을 못이으면 탈락, 해당 번호와 차례를 구함
# 두번째로 아까 했던 단어를 쓰면 탈락, 해당 번호와 차례를 구함