import sys

N = int(sys.stdin.readline()) # 가로세로 크기
maps = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)] # 2차원 배열로 저장

house = 1 # 단지의 총 개수
houses = [] # 단지내 집의 수를 저장할 배열

# 단지 하나씩 반복
while(True):
    h_temp = [] # 해당 단지내의 집의 위치 저장할 배열
    for x in range(N): # 단지에서 첫번째로 발견될 집의 위치를 찾음
        for y in range(N):
            if maps[x][y] == 1:
                h_temp.append((x,y))
                house += 1 # 해당 단지에 부여할 번호 (1과 구별하기 위해)
                maps[x][y] = house # 이미 발견한 집은 1과 구별
                break
        if h_temp: break
    if not h_temp: break # 더 이상 남은 집이 없으면 while문 탈출
        
    for h in h_temp: # 연결된 집 찾기
        x, y = h[0], h[1]
		# 지도 내에서 상하좌우로 연결된 집을 찾음, 찾으면 배열에 저장 후 구별
        if  x-1 > -1 and maps[x-1][y] == 1:
            h_temp.append((x-1, y))
            maps[x-1][y] = house
        if  y+1 < N and maps[x][y+1] == 1:
            h_temp.append((x, y+1))
            maps[x][y+1] = house
        if  x+1 < N and maps[x+1][y] == 1:
            h_temp.append((x+1, y))
            maps[x+1][y] = house
        if  y-1 > -1 and maps[x][y-1] == 1:
            h_temp.append((x, y-1))
            maps[x][y-1] = house
    houses.append(len(h_temp)) # 단지내 집의 수를 저장
    
print(house-1) # 총 단지수
houses.sort() # 단지내 집의 수 오름차순으로 정렬
print(*houses, sep='\n') # 단지내 집의 수 한줄씩 출력