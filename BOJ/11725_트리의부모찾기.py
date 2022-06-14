N = int(input())
nodes = [list(map(int, input().split())) for _ in range(N-1)]
results = [0 for _ in range(N)]
pop = [1]

while(pop):
    for i in range(N-1):
        if nodes[i][0] == pop[0]:
            results[nodes[i][1]-1] = pop[0]
            pop.append(nodes[i][1])
            nodes[i] = [-1,-1]
        elif nodes[i][1] == pop[0]:
            results[nodes[i][0]-1] = pop[0]
            pop.append(nodes[i][0])
            nodes[i] = [-1,-1]
    pop.pop(0)
            
for i in range(1, N): print(results[i])