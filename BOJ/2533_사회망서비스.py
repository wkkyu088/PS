import sys

N = int(sys.stdin.readline())
pairs = [list(map(int, sys.stdin.readline().split())) for _ in range(N-1)]

tree = {}
for i in range(1, N+1):
    tree[i] = [] 
for i in pairs:
    tree[i[0]].append(i[1])

countLeaf = 0
EA = 0
for i in tree.values():
    if not i:
        countLeaf = countLeaf + 1

rootLeaf = 0
if len(tree[1]) == countLeaf:
    EA = 1
else:
    for i in tree[1]:
        if not tree[i]: 
            rootLeaf = rootLeaf + 1
    EA = rootLeaf + (N - countLeaf - 1)
    
print(EA)