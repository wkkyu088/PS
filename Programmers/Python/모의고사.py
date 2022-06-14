def solution(answers):
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    num = [0,0,0,0]

    for i in range(len(answers)):
        if answers[i] == num1[i%len(num1)]:
            num[1] += 1
        if answers[i] == num2[i%len(num2)]:
            num[2] += 1
        if answers[i] == num3[i%len(num3)]:
            num[3] += 1

    answer = []
    maxA = max(num)
    for i in range(1, len(num)):
        if num[i] == maxA:
            answer.append(i)
    return answer