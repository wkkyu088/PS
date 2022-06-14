import sys
sys.setrecursionlimit(10**6)

global tree
tree = dict()

def make_tree(list):
    if len(list) > 1:
        root = list[0]
        if list[1] < root: left = 1
        else: left = -1
        right = -1

        for i in range(1, len(list)):
            if list[i] > root:
                right = i
                break
            
        if right == -1:
            tree[root] = [list[left], -1]
            make_tree(list[1:])
        elif left == -1:
            tree[root] = [-1, list[right]]
            make_tree(list[right:])
        else:
            tree[root] = [list[left], list[right]]
            make_tree(list[1:right])
            make_tree(list[right:])
    else:
        tree[list[0]] = [-1, -1]
        
def postorder(root):
    if root != -1:
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root)
    
line = None
list = []
for i in range(10000):
    line = sys.stdin.readline().rstrip()
    if line != '':
        list.append(int(line))
    else: break

make_tree(list)
postorder(list[0])