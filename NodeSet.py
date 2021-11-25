from typing import List

from Node import Node


class NodeSet:
    nodes : List[List[Node]] = None
    def __init__(self, nodes):
        self.nodes = nodes