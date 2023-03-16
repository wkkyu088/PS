def solution(board, moves):
    stack = [0]
    cnt = 0
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                if board[i][m-1] == stack[-1]:
                    cnt += 1
                    stack.pop()
                else: 
                    stack.append(board[i][m-1])
                board[i][m-1] = 0
                break
    return cnt*2