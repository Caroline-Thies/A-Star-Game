import sys
from typing import List
from Token import Token


class Node:
    def __init__(self, token, xy_coordinates, is_goal):
        self.token = token
        self.xyCoordinates = xy_coordinates
        self.isGoal = is_goal
        self.edges = []
        self.pathPredecessor = None
        self.stepsToReach = sys.maxsize

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
            token_push = TokenPush.TokenPush(free_token, i, self.parentSet, self)
            token_push_edges.append(Edge.Edge(self, token_push.activeNodeAfter, token_push))
        return self.edges.extend(token_push_edges)


class Edge:
    def __init__(self, source: Node, dest: Node, movement) -> None:
        self.source = source
        self.dest = dest
        self.movement = movement


class NodeSet:
    def __init__(self, nodes: List[List[Node]]):
        for i in range(len(nodes)):
            for j in range(len(nodes[i])):
                node = nodes[i][j]
                if i > 0:
                    left_node = nodes[i - 1][j]
                    if node.token.canReach["left"] and left_node.token.canReach["right"]:
                        node.edges.append(Edge(node, left_node, "LEFT"))
                if i < len(nodes) - 1:
                    right_node = nodes[i + 1][j]
                    if node.token.canReach["right"] and right_node.token.canReach["left"]:
                        node.edges.append(Edge(node, right_node, "RIGHT"))
                if j > 0:
                    up_node = nodes[i][j - 1]
                    if node.token.canReach["up"] and up_node.token.canReach["down"]:
                        node.edges.append(Edge(node, up_node, "UP"))
                if j < len(nodes[i]) - 1:
                    down_node = nodes[i][j + 1]
                    if node.token.canReach["down"] and down_node.token.canReach["up"]:
                        node.edges.append(Edge(node, down_node, "DOWN"))
        self.nodes = nodes

    def __str__(self):
        result = ""
        for row in self.nodes:
            row1, row2, row3 = "", "", ""
            for node in row:
                row1 += node.token.str_row1()
                row2 += node.token.str_row2()
                row3 += node.token.str_row3()
            result += row1 + "\n" + row2 + "\n" + row3 + "\n"
        return result


class TokenPush:
    pushedToken: Token = None
    row: int = 0
    oldSet: NodeSet = None
    newSet: NodeSet = None
    freedToken: Token = None
    activeNodeBefore: Node = None
    activeNodeAfter: Node = None

    def __init__(self,
                 pushed_token: Token,
                 row: int,
                 old_set: NodeSet,
                 active_node_before: Node):
        self.pushedToken = pushed_token
        self.row = row
        self.oldSet = old_set
        self.activeNodeBefore = active_node_before
        self.newSet, self.freedToken = self.calc_new_set(old_set, pushed_token, row)

    def __str__(self):
        return "Pushing Token in Row " + str(self.row)

    def calc_new_set(self, old_set: NodeSet, pushed_token: Token, row: int):
        return old_set, pushed_token
