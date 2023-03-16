def solution(str1, str2):
    answer = 0
    
    str1 = str1.upper()
    str2 = str2.upper()
    list1 = []
    list2 = []
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            list1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            list2.append(str2[i:i+2])
    # print(list1, list2)
    
    inter = []
    union = []
    for i in list1:
        for j in list2:
            if i == j:
                inter.append(i)
            elif i[0]==j[0] or i[1]==j[0] or i[0]==j[1] and i[1]==j[1]:
                union.append(i)
                union.append(j)
    print(inter)
    print(union)
    
    return answer

solution('FRANCE', 'french')
print()
# solution('handshake', 'shake hands')
# print()
solution('aa1+aa2', 'AAAA12')
# print()
# solution('E=M*C^2', 'e=m*c^2')