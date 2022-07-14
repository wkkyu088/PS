from itertools import combinations

def isPrime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def solution(nums):
    cnt = 0
    comb = list(combinations(nums, 3))
    for c in comb:
        if(isPrime(c[0]+c[1]+c[2])):
            cnt += 1
    return cnt