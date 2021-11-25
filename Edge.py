from Node import Node


class Edge:
    source : Node = None
    dest : Node = None
    movement = None
    def __init__(self, source: Node, dest : Node, movement) -> None:
        self.source = source
        self.dest = dest
        self.movement = movement 