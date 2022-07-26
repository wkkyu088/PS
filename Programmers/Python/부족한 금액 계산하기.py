def solution(price, money, count):
    for i in range(count):
        money = money - price*(i+1)
    if money < 0:
        answer = -money
    else: 
        answer = 0

    return answer

def solution(price, money, count):
    answer = sum(range(price, price*count+1, price)) - money
    return answer if answer>0 else 0

def solution(price, money, count):
    return max(0, count*price*(count+1)//2-money)
