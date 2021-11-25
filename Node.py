from _typeshed import StrOrBytesPath
from typing import List
from Edge import Edge
from NodeSet import NodeSet
from Token import Token

import sys

from TokenPush import TokenPush

class Node:
    token: Token = None
    edges : List[Edge] = None
    xyCoordinates = {"x" : 0, "y" : 0}
    isGoal : bool = None
    stepsToReach : int = sys.maxsize
    pathPredecessor = None
    parentSet : NodeSet = None
    
    def __init__(self, parentSet, token, edges, xyCoordinates, isGoal):
        self.parentSet = parentSet
        self.token = token
        self.edges = edges
        self.xyCoordinates = xyCoordinates
        self.isGoal = isGoal

    def getCosts(self, goalCoordinates):
        xDistance = self.xyCoordinates.x - goalCoordinates.x
        yDistance = self.xyCoordinates.y - goalCoordinates.y
        absDistance = abs(xDistance) + abs(yDistance)
        return self.stepsToReach + absDistance
    def updateStepsToReach(self, newStepsToReach, node):
        if newStepsToReach < newStepsToReach:
            self.pathPredecessor = node
            self.stepsToReach = newStepsToReach
    def getEdges(self, freeToken):
        tokenPushEdges = []
        for i in range(1, 6):
            tokenPush = TokenPush(freeToken, i, self.parentSet, self)
            tokenPushEdges.append(Edge(self, tokenPush.activeNodeAfter, tokenPush))
        return self.edges.extend(tokenPushEdges)