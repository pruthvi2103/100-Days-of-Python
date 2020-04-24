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


# Insert function
def BTreeinsert(node,val):
    if node.value < val:
        if node.rightNode == None:
            node.rightNode = Node(val)
          #  print("inserted right")
        else:
            
            BTreeinsert(node.rightNode,val)
    

    if node.value > val:
        if node.leftNode == None:
            node.leftNode = Node(val)
           # print("inserted left")
        else:
            
            BTreeinsert(node.leftNode,val)

#def BTreeprint(node):

    

inp=input("Enter comma seperated values to be converted to binary tree").split(',')

tree = BinaryTree(inp[0])
inp.pop(0)
print(tree.root.value)

for x in inp:
    spec = tree.root
    BTreeinsert(spec,x)
print(tree.root.leftNode.rightNode.value)
        

         







