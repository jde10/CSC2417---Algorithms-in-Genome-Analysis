import numpy as np
class Node:
    def __init__(self, visited=0, reward=0, action=[], state=[[],[]], i=0, j=0, left=None, middle=None, right=None, parent=None):
        # type: (visited: int, reward: int, action: list, state: np.array, i: int, j: int,
        #  Node, Node, Node, Node) -> object
        """

        :type visited: int
        """
        self.N = visited
        self.Q = reward
        self.a = action
        self.s = state
        self.i = i
        self.j = j
        self.leftChild = left
        self.rightChild = right
        self.middleChild = middle
        self.parent = parent
        self.possibleChildren = False

    def hasLeftChild(self):
        if self.leftChild is not None:
            return True
        else:
            return False

    def hasRightChild(self):
        if self.rightChild is not None:
            return True
        else:
            return False

    def hasMiddleChild(self):
        if self.middleChild is not None:
            return True
        else:
            return False

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isMiddleChild(self):
        return self.parent and self.parent.middleChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild or self.middleChild)

    def hasAnyChildren(self):
        return (self.rightChild or self.leftChild or self.middleChild)

    def hasTwoChildren(self):
        if (self.rightChild is not None) and (self.leftChild is not None):
            return True
        if (self.rightChild is not None) and (self.middleChild is not None):
            return True
        if (self.middleChild is not None) and (self.leftChild is not None):
            return True
        else:
            return False

    def hasMidandRightChildren(self):
        if (self.rightChild is not None) and (self.middleChild is not None):
            return True
        else:
            return False

    def hasThreeChildren(self):
        if (self.rightChild is not None) and (self.leftChild is not None) and (self.middleChild is not None):
            return True
        else:
            return False

    def hasPossibleChildren(self):
        return self.possibleChildren

    def getCharIni(self):
        return self.i

    def getCharInj(self):
        return self.j

    def getState(self):
        return self.s

    def getVisited(self):
        return self.N

    def getReward(self):
        return self.Q

    def replaceNodeData(self, visited, reward, action, state, i, j, lc, rc, mc):
        self.N = visited
        self.Q = reward
        self.a = action
        self.s = state
        self.i = i
        self.j = j
        self.leftChild = lc
        self.rightChild = rc
        self.middleChild = mc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
        if self.hasMiddleChild():
           self.middleChild.parent = self