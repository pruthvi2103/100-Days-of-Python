#binaary tree
#my own take on a binary tree
class Node(object):
        def __init__(self,value):
                self.value = value
                self.leftNode= None
                self.rightNode = None
       

class BinaryTree():
    def __init__(self,root):
        self.root=Node(root)

inp=input("Enter comma seperated values to be converted to binary tree").split(',')

tree = BinaryTree(inp[0])
inp.pop(0)

print (tree.root.value + 1)

# for x in tree:
#     if x > int(tree.root.value):




