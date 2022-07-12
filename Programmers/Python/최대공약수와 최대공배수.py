def solution(n, m):
    x = 0
    y = 0
    
    # 최대공약수
    for i in range(1, min(n, m)+1):
        if n%i==0 and m%i==0:
            x = i
    
    #최소공배수
    for i in range(1, n*m):
        if (n*m+1-i)%n==0 and (n*m+1-i)%m==0:
            y = n*m+1-i
            
    return [x, y]