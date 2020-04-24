#binaary tree
#my own take on a binary tree
# Class Node defines a specific node, having properties: 
#   value: which has the value stored in each node
#   leftNode:   which has the node stored on the left
#   rightNode:  which has the node stored on the Right
# 
# Class BinaryTree is the main binary tree 
#   it has input method for input
#   and preorder method denotes Preorder traversal and prints the pre order route
#  
class Node(object):
        def __init__(self,value):
                self.value = value
                self.leftNode= None
                self.rightNode = None
       

class BinaryTree():
    def __init__(self,root):
        self.root=Node(root)

    def print_tree(self, traversal_type):
        
        if traversal_type == "preorder":
            return self.preorder_print(tree.root,"")
    # Insert function
    def insert(self,node,val):
        if node.value < val:
            if node.rightNode == None:
                node.rightNode = Node(val)
          #  print("inserted right")
            else:
            
                self.insert(node.rightNode,val)
    

        if node.value > val:
            if node.leftNode == None:
                node.leftNode = Node(val)
           # print("inserted left")
            else:
            
                self.insert(node.leftNode,val)

    def preorder_print(self,start,traversal):
        if start:
            traversal += (str(start.value) + "->")
            traversal = self.preorder_print(start.leftNode,traversal)
            traversal = self.preorder_print(start.rightNode,traversal)
        return traversal

#def BTreeprint(node):

    
# driver code
#def main() :
inp=input("Enter comma seperated values to be converted to binary tree:  ").split(',')

tree = BinaryTree(inp[0])
inp.pop(0)
# print(tree.root.value)

for x in inp:
    spec = tree.root
    tree.insert(spec,x)
#print(tree.root.leftNode.rightNode.value)
print(tree.print_tree("preorder").rstrip('->'))
        

#if __name__ == "__main__":
#    main()

         

# Made by Pruthvi Shetty as a part of the 100 days of python challange  on 23-04-2020





