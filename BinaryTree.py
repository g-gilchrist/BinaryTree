#==============================================================================
#    Author: Grant Gilchrist
#    Problem: create the below tree and print nodes 003, 004, 006 and 010.
#==============================================================================
#       TREE STRUCTURE:
#            (003)
#            /   \
#         (002) (004)
#                  \
#                 (006)
#                 /   \
#              (005) (010)


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def add(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.add(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.add(data)

    def PrintTree(self):
       # if self.left:
       #     self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

root = Node('003')
root.add('002')
root.add('004')
root.add('006')
root.add('005')
root.add('010')

root.PrintTree()