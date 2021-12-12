import copy
import random
import sys
from typing import List

import Model
from Token import Token


# To avoid circular imports, all these classes must be in one file

class Node:
    def __init__(self, token, row, col, is_goal, parent_set=None):
        self.token = token
        self.row = row
        self.col = col
        self.isGoal = is_goal
        self.edges = []
        self.token_pushes_calculated = False
        self.path_in_edge = None
        self.stepsToReach = sys.maxsize
        self.parent_set = parent_set

    def __str__(self):
        return "S" + str(self.parent_set.id) + " R" + str(self.row) \
               + " C" + str(self.col) + " $" + str(self.get_costs())

    def __lt__(self, other):
        return self.get_costs() < other.get_costs()

    def get_costs(self):
        goal_row = self.parent_set.dest_row
        goal_col = self.parent_set.dest_col
        row_distance = self.row - goal_row
        col_distance = self.col - goal_col
        abs_distance = abs(row_distance) + abs(col_distance)
        return self.stepsToReach + abs_distance

    def update_steps_to_reach(self, new_steps_to_reach, edge):
        if new_steps_to_reach < self.stepsToReach:
            self.path_in_edge = edge
            self.stepsToReach = new_steps_to_reach

    def get_edges(self):
        if self.token_pushes_calculated:
            return self.edges
        free_token = self.parent_set.free_token
        token_push_edges = []
        for i in range(1, 5):
            token_push = TokenPush(free_token, i, self.parent_set, self)
            edge = Edge(self, token_push.activeNodeAfter, token_push)
            token_push_edges.append(edge)
        self.edges.extend(token_push_edges)
        self.token_pushes_calculated = True
        return self.edges

    def set_parent_set(self, parent_set):
        self.parent_set = parent_set

    def get_is_valid_goal(self):
        if self.isGoal:
            print("goal node reached")
        return self.isGoal and self.token.canReach["up"]

    def get_token(self):
        if self.token is not None:
            return self.token
        else:
            print("Empty Token on node")
            return Token(False, False, False, False)


class Edge:
    def __init__(self, source: Node, dest: Node, movement) -> None:
        self.source = source
        self.dest = dest
        self.movement = movement

    def __str__(self):
        return str(self.movement) + \
               " from R" + str(self.source.row) + \
               " C" + str(self.source.col) + " to R" + \
               str(self.dest.row) + " C" + str(self.dest.col)


class NodeSet:
    total_nodesets = 0

    def __init__(self, nodes: List[List[Node]], free_token: Token, dest_row: int, dest_col: int):
        self.nodes = nodes
        for row in range(len(nodes)):
            for col in range(len(nodes[row])):
                node = nodes[row][col]
                node.set_parent_set(self)
                if col > 0:
                    left_node = nodes[row][col - 1]
                    if node.get_token().canReach["left"] and left_node.get_token().canReach["right"]:
                        node.edges.append(Edge(node, left_node, "LEFT"))
                if col < len(nodes[row]) - 1:
                    right_node = nodes[row][col + 1]
                    if node.get_token().canReach["right"] and right_node.get_token().canReach["left"]:
                        node.edges.append(Edge(node, right_node, "RIGHT"))
                if row > 0:
                    up_node = nodes[row - 1][col]
                    if node.get_token().canReach["up"] and up_node.get_token().canReach["down"]:
                        node.edges.append(Edge(node, up_node, "UP"))
                if row < len(nodes) - 1:
                    down_node = nodes[row + 1][col]
                    if node.get_token().canReach["down"] and down_node.get_token().canReach["up"]:
                        node.edges.append(Edge(node, down_node, "DOWN"))
        self.free_token = free_token
        self.dest_row = dest_row
        self.dest_col = dest_col
        self.id = NodeSet.total_nodesets
        NodeSet.total_nodesets += 1

    def __str__(self):
        result = ""
        for row in self.nodes:
            row1, row2, row3 = "", "", ""
            for node in row:
                row1 += node.get_token().str_row1()
                row2 += node.get_token().str_row2(is_goal=node.isGoal)
                row3 += node.get_token().str_row3()
            result += row1 + "\n" + row2 + "\n" + row3 + "\n"
        return result

    def __eq__(self, other):
        return self.id == other.id


def get_nodelist_deepcopy(nodelist: List[Node]):
    list_copy = []
    for node in nodelist:
        list_copy.append(Node(node.token, node.row, node.col, node.isGoal))
    return list_copy


def calc_new_set(old_set: NodeSet, pushed_token: Token, row: int):
    new_nodes: List[List[Node]] = []
    freed_token: Token = None
    for row_index in range(len(old_set.nodes)):
        row_deepcopy = get_nodelist_deepcopy(old_set.nodes[row_index])
        if row_index == row and row_index % 2 == 0:
            freed_token = push_to_right(row_deepcopy, pushed_token)
        elif row_index == row and row_index % 2 == 1:
            freed_token = push_to_left(row_deepcopy, pushed_token)
        new_nodes.append(row_deepcopy)
    return NodeSet(new_nodes, freed_token, old_set.dest_row, old_set.dest_col)


def push_to_left(nodes: List[Node], token: Token):
    freed_token = nodes[0].get_token()
    for i in range(len(nodes) - 1):
        nodes[i].token = nodes[i + 1].get_token()
    nodes[-1].token = token
    return freed_token


def push_to_right(nodes, token):
    freed_token = nodes[-1].get_token()
    for i in range(1, len(nodes)):
        index = len(nodes) - i
        nodes[index].token = nodes[index - 1].token
    nodes[0].token = token
    return freed_token


def calc_active_node_after(new_node_set, row, active_node_before):
    new_col = active_node_before.col
    if row == active_node_before.row and row % 2 == 0:
        new_col = active_node_before.col + 1
        if new_col > len(new_node_set.nodes[0]) - 1:
            new_col = 0
    elif row == active_node_before.row and row % 2 == 1:
        new_col = active_node_before.col - 1
        if new_col < 0:
            new_col = len(new_node_set.nodes[0]) - 1
    return new_node_set.nodes[active_node_before.row][new_col]


class TokenPush:
    def __init__(self,
                 pushed_token: Token,
                 row: int,
                 old_set: NodeSet,
                 active_node_before: Node):
        self.pushedToken = pushed_token
        self.row = row
        self.oldSet = old_set
        self.activeNodeBefore = active_node_before
        self.newSet = calc_new_set(old_set, pushed_token, row)
        self.freedToken = self.newSet.free_token
        self.activeNodeAfter = calc_active_node_after(self.newSet, row, active_node_before)

    def __str__(self):
        return "PUSH TOKEN in Row " + str(self.row)
