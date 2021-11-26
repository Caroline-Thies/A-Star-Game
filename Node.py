from _typeshed import StrOrBytesPath
from typing import List
from Edge import Edge
from NodeSet import NodeSet
from Token import Token

import sys

from TokenPush import TokenPush


class Node:
    def __init__(self, token, xy_coordinates, is_goal):
        self.token = token
        self.xyCoordinates = xy_coordinates
        self.isGoal = is_goal
        self.edges = []

    def __str__(self):
        return str(self.token) + self.isGoal

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
