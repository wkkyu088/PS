def solution(n):
    # 변환한 3진수를 저장할 변수
    T = '' 
    
    # 3진수 변환
    while n > 0:
        x = divmod(n, 3)
        n = x[0]
        T += str(x[1])
        
    # 10진수 변환하여 반환
    return int(T, 3)
