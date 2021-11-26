from _typeshed import StrOrBytesPath
from typing import List
from Edge import Edge
from NodeSet import NodeSet
from Token import Token

import sys

from TokenPush import TokenPush


class Node:
    token: Token = None
    edges: List[Edge] = None
    xyCoordinates = {"x": 0, "y": 0}
    isGoal: bool = None
    stepsToReach: int = sys.maxsize
    pathPredecessor = None
    parentSet: NodeSet = None

    def __init__(self, parent_set, token, xy_coordinates, is_goal):
        self.parentSet = parent_set
        self.token = token
        self.xyCoordinates = xy_coordinates
        self.isGoal = is_goal
        self.edges = []

    def get_costs(self, goal_coordinates):
        x_distance = self.xyCoordinates.x - goal_coordinates.x
        y_distance = self.xyCoordinates.y - goal_coordinates.y
        abs_distance = abs(x_distance) + abs(y_distance)
        return self.stepsToReach + abs_distance

    def update_steps_to_reach(self, new_steps_to_reach, node):
        if new_steps_to_reach < new_steps_to_reach:
            self.pathPredecessor = node
            self.stepsToReach = new_steps_to_reach

    def get_edges(self, free_token):
        token_push_edges = []
        for i in range(1, 6):
            token_push = TokenPush(free_token, i, self.parentSet, self)
            token_push_edges.append(Edge(self, token_push.activeNodeAfter, token_push))
        return self.edges.extend(token_push_edges)
