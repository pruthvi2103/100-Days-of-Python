class Stack(object):
    
    def __init__(self,value):
        self.stack = []
        self.stack.insert(self,value)

    def insert(self,value):
        self.append(value)
    def delete(self):
        self.pop()

a = Stack(1)
str(a.stack)
a.insert(5)
a.insert(3)
str(a.stack)
a.delete
str(a.stack)