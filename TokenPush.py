from Node import Node
from NodeSet import NodeSet
from Token import Token


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
