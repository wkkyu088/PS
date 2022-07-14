def solution(s):
    w = list(s)
    cnt = 0
    for i in range(len(w)):
        if w[i] == " ":
            cnt = 0
        else:
            w[i] = w[i].upper() if cnt%2==0 else w[i].lower()
            cnt += 1     
    return ''.join(w)