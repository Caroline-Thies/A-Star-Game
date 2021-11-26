import csv
from typing import List

from Node import Node
from NodeSet import NodeSet
from Token import Token

GOAL_X_COORDINATE = 0
GOAL_Y_COORDINATE = 4

tokenDict = {
    0: Token(False, True, False, True),
    1: Token(True, False, False, True),
    2: Token(False, True, True, False),
    3: Token(True, False, True, False),
    4: Token(True, True, False, True),
    5: Token(True, False, True, True),
    6: Token(True, True, True, False),
    7: Token(False, True, True, True),
    8: Token(False, False, True, True),
    9: Token(True, True, False, False)
}


def get_nodeset_and_free_token_from_file(filepath: str):
    nodes: List[Node] = []
    free_token: Token
    with open(filepath) as csvFile:
        csv_reader = csv.reader(csvFile)
        for row, row_index in csv_reader:
            if row_index < len(row) - 1:
                for item, item_index in row:
                    is_goal = row_index == GOAL_X_COORDINATE and item_index == GOAL_Y_COORDINATE
                    nodes.append(Node(tokenDict[item], [row_index, item_index], is_goal))
            else:
                free_token = tokenDict[row[0]]
    return NodeSet(nodes), free_token
