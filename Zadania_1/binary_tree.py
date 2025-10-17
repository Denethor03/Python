class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.left_weight = None
        self.right_weight = None

class Tree():
    def __init__(self):
        self.root = None

    def addRoot(self,value):
        self.root = Node(value)
        return self.root
    
    def addLeft(self,parent,value,weight):
        child = Node(value)
        parent.left = child
        parent.left_weight = weight
        return child
    
    def addRight(self,parent,value,weight):
        child = Node(value)
        parent.right = child
        parent.right_weight = weight
        return child
    def Traverse(self,node=None):
        if node is None:
            node = self.root
        # pre order travelsal
        print(node.value)
        if node.left: #if not none
            self.Traverse(node.left)
        if node.right:
            self.Traverse(node.right)
        
    def __str__(self):
        def makeTree(node=None,level=0,weigth=0):
            if node is None:
                node = self.root
            if level ==0:
                line = node.value+"\n"
            else:
                line = level*"  "+f"-{weigth}""->"+f"{node.value}\n"
                #print(level*"  "+f"-{weigth}""->"+f"{node.value}")
            if node.left:
                line+=makeTree(node.left,level+1,node.left_weight)
                #self.__str__(node.left,level+1,node.left_weight)
            if node.right:
                line+=makeTree(node.right,level+1,node.right_weight)
                #self.__str__(node.right,level+1,node.right_weight)
            return line
        return makeTree()


tree = Tree()
root = tree.addRoot('R')
A = tree.addLeft(root,'A',1)
B = tree.addRight(root,'B',3)
C = tree.addLeft(A,'C',1)
D = tree.addRight(A,'D',1)
E = tree.addLeft(B,'E',3)
F = tree.addRight(B,'F',4)
G = tree.addLeft(E,"G",0)
print(tree)
tree.Traverse()
