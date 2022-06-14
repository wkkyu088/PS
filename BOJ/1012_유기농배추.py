import sys

T = int(sys.stdin.readline()) # 테스트 케이스
M, N, K = map(int, sys.stdin.readline().split()) # 배추밭 가로, 세로, 배추의 위치의 개수
items = [list(map(int, sys.stdin.readline().split())) for _ in range(K)] # 배추의 위치들
land = [[0 for _ in range(M)] for _ in range(N)] # 배추밭
for i in items: # 배추밭에 배추 심기
    land[i[1]][i[0]] = 1

print('#CABBAGE')
for i in land:
    print(*i)
    