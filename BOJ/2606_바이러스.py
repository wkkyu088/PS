import sys

num = int(sys.stdin.readline()) # 컴퓨터 개수
pair = int(sys.stdin.readline()) # 연결쌍 수
pairs = [list(map(int, sys.stdin.readline().split())) for _ in range(pair)] # 번호쌍 리스트

infected = [1] # 감염된 컴퓨터 배열
for i in infected:
    for p in pairs:
        if p[0]==i and p[1] not in infected:
            infected.append(p[1])
        elif p[1]==i and p[0] not in infected:
            infected.append(p[0])
print(len(infected)-1) # 결과 값