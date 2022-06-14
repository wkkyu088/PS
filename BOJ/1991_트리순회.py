import sys

N = int(sys.stdin.readline())
tree = dict()

for i in range(N):
    p, left, right = map(str, sys.stdin.readline().split())
    if i == 0: root = p
    tree[p] = [left, right]

def pre(root):
    if root != '.':
        print(root)
        pre(tree[root][0])
        pre(tree[root][1])

def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root)
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root)

print("inorder")
pre(root)
print("postorder")
postorder(root)