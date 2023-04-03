def solution(t):
    for i in range(1, len(t)):
        for j in range(len(t[i])):
            if j == 0:
                t[i][j] += t[i-1][j]
            elif j == len(t[i])-1:
                t[i][j] += t[i-1][j-1]
            else:
                t[i][j] += max(t[i-1][j], t[i-1][j-1])
    return max(t[-1])