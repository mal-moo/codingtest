"""
    data structure: #tree
    understand: n
    link: https://www.acmicpc.net/problem/5639
"""

import sys
sys.setrecursionlimit(20000)  # ?

input = sys.stdin.readline()


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
    
    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        
        else:
            current = self.root
            while True:
                if current.data > data:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    current = current.left

                if current.data < data:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    current = current.right
    
    def post_order(self, node=None):
        #global answer
        answer = []
        if node is None:
            node = self.root
        
        if node.left is not None:
            self.post_order(node.left)
        if node.right is not None:
            self.post_order(node.right)
        answer.append(node.data)

        return answer

tree = Tree() 
while True:
    try:
        tree.add(int(input()))
    except:
        break 

answer = tree.post_order()
print('\n'.join(map(str, answer)))