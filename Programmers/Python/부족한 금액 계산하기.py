def solution(price, money, count):
    for i in range(count):
        money = money - price*(i+1)
    if money < 0:
        answer = -money
    else: 
        answer = 0

    return answer