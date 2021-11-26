from typing import List

from Edge import Edge
from Node import Node


class NodeSet:
    nodes: List[List[Node]] = None

    def __init__(self, nodes: List[List[Node]]):
        for i in range(len(nodes)):
            for j in range(len(nodes[i])):
                node = nodes[i][j]
                if i > 0:
                    left_node = nodes[i - 1][j]
                    if node.token.canReach.left and left_node.token.canReach.right:
                        node.edges.append(Edge(node, left_node, "LEFT"))
                if i < len(nodes) - 1:
                    right_node = nodes[i + 1][j]
                    if node.token.canReach.right and right_node.token.canReach.left:
                        node.edges.append(Edge(node, right_node, "RIGHT"))
                if j > 0:
                    up_node = nodes[i][j - 1]
                    if node.token.canReach.up and up_node.token.canReach.down:
                        node.edges.append(Edge(node, up_node, "UP"))
                if j < len(nodes[i]) - 1:
                    down_node = nodes[i][j + 1]
                    if node.token.canReach.down and down_node.token.canReach.up:
                        node.edges.append(Edge(node, down_node, "DOWN"))
        self.nodes = nodes
