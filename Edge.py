from Node import Node


class Edge:
    def __init__(self, source: Node, dest: Node, movement) -> None:
        self.source = source
        self.dest = dest
        self.movement = movement
