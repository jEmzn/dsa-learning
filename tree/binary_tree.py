import operator

class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    # insert newNode at subtree
    def insertLeft(self, newNode):
        if self.leftChild == None:  # if leftChild is None, creat newNode at leftChild
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode) # if leftChild is not None, creat a newNode and 
            t.leftChild = self.leftChild    # set the newNode's leftChild is oldLeftChild
            self.leftChild = t  # oldLeftChild become newNode

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key
    
    # def getRightChildKey(self):
    #     if self:
    #         return self.getRightChild().key
    #     return None
    
    # def getLeftChildKey(self):
    #     if self:
    #         return self.getLeftChild().key
    #     return None
    
    # Traversal
    def preorder(self, tree):
        if tree:
            print(tree.getRootVal())
            self.preorder(tree.getLeftChild())
            self.preorder(tree.getRightChild())

    def postorder(self, tree):
        if tree != None:
            self.postorder(tree.getLeftChild())
            self.postorder(tree.getRightChild())
            print(tree.getRootVal())

    def postordereval(self, tree):
        opers = {'+':operator.add,
                 '-':operator.sub,
                 '*':operator.mul,
                 '/':operator.truediv}
        res1 = None
        res2 = None
        if tree:
            res1 = tree.postordereval(tree.getLeftChild())
            res2 = tree.postordereval(tree.getRightChild())
            if res1 and res2:
                return opers[tree.getRootVal()](res1, res2)
            else:
                return tree.getRootVal()
            
    def inorder(self, tree):
        if tree != None:
            tree.inorder(tree.getLeftChild())
            print(tree.getRootVal())
            tree.inorder(tree.getRightChild())

    def printexp(self, tree):
        sVal = ""
        if tree:
            sVal = '(' + tree.printexp(tree.getLeftChild())
            sVal = sVal + str(tree.getRootVal())
            sVal = sVal + tree.printexp(tree.getRightChild()) + ')'
        return sVal

    
