# https://www.acmicpc.net/problem/1991
# 이름 : 트리 순회
# 번호 : 1991
# 난이도 : 실버 I
# 분류 : 트리, 재귀

import sys
input = sys.stdin.readline
N = int(input())
tree = {}
for _ in range(N):
    root, left, right = input().strip().split()
    tree[root] = (left, right)

def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right
 
def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right
 
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root

preorder('A')
print()
inorder('A')
print()
postorder('A')