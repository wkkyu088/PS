def solution(numbers, hand):
    answer = ''
    pos = {1:(-1,1), 2:(0,1), 3:(1,1), 
            4:(-1,2), 5:(0,2), 6:(1,2), 
            7:(-1,3), 8:(0,3), 9:(1,3), 0:(0,4)}
    now = [[-1,4], [1,4]]
    for n in numbers:
        if n in (1, 4, 7):
            answer += 'L'
            now[0] = pos[n]
        elif n in (3, 6, 9):
            answer += 'R'
            now[1] = pos[n]
        else:
            dL = abs(pos[n][0]-now[0][0])+abs(pos[n][1]-now[0][1])
            dR = abs(pos[n][0]-now[1][0])+abs(pos[n][1]-now[1][1])
            if dL < dR:
                answer += 'L'
                now[0] = pos[n]
            elif dL > dR:
                answer += 'R'
                now[1] = pos[n]
            else:
                if hand=='left':
                    answer += 'L'
                    now[0] = pos[n]
                else:
                    answer += 'R'
                    now[1] = pos[n]
    return answer