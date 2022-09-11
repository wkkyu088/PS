from itertools import combinations

def solution(orders, course):
    sets = {}
    for c in course:
        sets[c] = {}
            
    for o in orders:
        for c in course:
            for comb in combinations(o, c):
                menu = ''.join(sorted(comb))
                if menu in sets[len(menu)]:
                    sets[len(menu)][menu] += 1
                else:
                    sets[len(menu)][menu] = 1
        
    maxN = []
    for c in course:
        if sets[c].values() and max(sets[c].values()) > 1:
            maxN.append([c, max(sets[c].values())])
    
    answer = []
    for i in range(len(maxN)):
        for k in sets[maxN[i][0]].keys():
            if sets[maxN[i][0]][k] == maxN[i][1]:
                answer.append(k)
    
    return sorted(answer)