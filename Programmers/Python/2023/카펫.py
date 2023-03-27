import math

def solution(brown, yellow):
    a, b, c = 1, (-4-brown)/2, brown+yellow
    return [int((-b+math.sqrt(b**2-4*a*c))/2*a), int((-b-math.sqrt(b**2-4*a*c))/2*a)]