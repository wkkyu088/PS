def solution(people, limit):
    answer = 0
    people = sorted(people)
    head = 0
    try:
        for i in range(len(people)):
            if people[head]+people[-1]<=limit:
                answer += 1
                head += 1
                people.pop()
            else:
                answer += 1
                people.pop()
    except:
        print()
    return answer