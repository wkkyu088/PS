def solution(n):
    x = 1
    while True:
        if n % x == 1:
            return x
        x += 1
        
def solution(n):
    for i in range(1, n):
        if n%i==1: return i