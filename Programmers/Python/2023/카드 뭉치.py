def solution(cards1, cards2, goal):
    answer = "Yes"
   
    for g in goal:
        temp = ''
        if cards1 and cards1[0] == g:
            temp = cards1.pop(0)
        elif cards2 and cards2[0] == g:
            temp = cards2.pop(0)
        
        if not temp:
            return "No"
    
    return answer