def solution(rows, columns, queries):
    answer = [[(j-1)*rows + i for i in range(1, columns+1)] for j in range(1, rows+1)]
    # for a in answer:
    #     print(a)
    
    for q in queries:
        print(q)
        x1, y1, x2, y2 = q
        t = answer[x1-1][y1-1]
        # print()
        
        for i in range(x2-x1):
            if 0 <= x1+i-1 < rows:
                answer[x1+i-1][y1-1] = answer[x1+i][y1-1]
            # print(answer[x1+i-1][y1-1], (x1+i-1, y1-1))
        # for a in answer:
        #     print(a)
        # print()
        
        for i in range(y2-y1):
            if 0 <= y1+i-1 < columns:
                answer[x2-1][y1+i-1] = answer[x2-1][y1+i]
            # print(answer[x2-1][y1+i-1], (x2-1, y1+i-1))
        # for a in answer:
        #     print(a)
        # print()
        
        for i in range(x2-x1):
            if 0 <= x2-i-2 < rows:
                answer[x2-i-1][y2-1] = answer[x2-i-2][y2-1]
            # print(answer[x2-i-1][y2-1], (x2-i-1, y2-1))
        # for a in answer:
        #     print(a)
        # print()
        
        for i in range(y2-y1):
            if 0 <= y2-i < columns:
                answer[x1-1][y2-i] = answer[x1-1][y2-i-1]
            # print(answer[x1-1][y2-i-1], (x1-1, y2-i-1))
        answer[x1-1][y1] = t
        for a in answer:
            print(a)
        print()
        
            
            
    return answer

# solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])
solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])
# solution(100, 97, [[1,1,100,97]])


# (2, 2) -> [ (2, 4) ] -> (5, 4) -> [ (5, 2) ]
# (x1, y1) <- (x1, y2) <- (x2, y2) <- (x2, y1)

			
# (2, 2) - (2, 3) 			=> plus Y
# - (2, 4) - (3, 4) - (4, 4) 	=> plus X
# (5, 4) - (5, 3)			=> minus Y
# - (5, 2) - (4, 2) - (3, 2)	=> minus X


# (1, 1) (1, 2) (1, 3) (1, 4) (1, 5) (1, 6)
# (2, 1) (2, 2) (2, 3) (2, 4) (2, 5) (2, 6)
# (3, 1) (3, 2) (3, 3) (3, 4) (3, 5) (3, 6)
# (4, 1) (4, 2) (4, 3) (4, 4) (4, 5) (4, 6)
# (5, 1) (5, 2) (5, 3) (5, 4) (5, 5) (5, 6)
# (6, 1) (6, 2) (6, 3) (6, 4) (6, 5) (6, 6)