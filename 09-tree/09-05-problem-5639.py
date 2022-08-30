"""
    data structure: #tree
    understand: y
    link: https://www.acmicpc.net/problem/5639
"""

import sys

sys.setrecursionlimit(20000)


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
        
    def post_order(self, node=None, post_data=None):
        if post_data is None:
            post_data = []
        
        if node is None:
            node = self.root
        
        if node.left is not None:
            self.post_order(node.left, post_data)
        if node.right is not None:
            self.post_order(node.right, post_data)
        
        post_data.append(node.data)

        return post_data


tree = Tree() 

while True:
    try:
        tree.add(int(input()))
    except:
        break 

post_data = tree.post_order()

print('\n'.join(map(str, post_data)))