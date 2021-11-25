from Node import Node
from NodeSet import NodeSet
from Token import Token


class TokenPush:
    pushedToken : Token = None
    row : int = 0
    oldSet : NodeSet = None
    newSet : NodeSet = None
    freedToken : Token = None
    activeNodeBefore : Node = None
    activeNodeAfter : Node = None
    def __init__(self, 
                pushedToken : Token, 
                row: int, 
                oldSet : NodeSet, 
                activeNodeBefore : Node):
        self.pushedToken = pushedToken
        self.row = row
        self.oldSet = oldSet
        self.activeNodeBefore = activeNodeBefore
        self.newSet, self.freedToken = self.calcNewSet(oldSet, pushedToken, row)
    
    def __str__(self):
        return "Pushing Token in Row " + str(self.row)

    def calcNewSet(self, oldSet : NodeSet, pushedToken : Token, row : int):
        pass