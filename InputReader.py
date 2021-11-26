import csv
from typing import List

from Model import NodeSet, Node
from Token import Token

GOAL_COL = 3
GOAL_ROW = 0

tokenDict = {
    "0": Token(False, True, False, True),
    "1": Token(True, False, False, True),
    "2": Token(False, True, True, False),
    "3": Token(True, False, True, False),
    "4": Token(True, True, False, True),
    "5": Token(True, False, True, True),
    "6": Token(True, True, True, False),
    "7": Token(False, True, True, True),
    "8": Token(False, False, True, True),
    "9": Token(True, True, False, False)
}


def get_nodeset_and_free_token_from_file(filepath):
    nodes: List[List[Node]] = []
    free_token: Token = Token(False, False, False, False)
    with open(filepath) as csvFile:
        csv_reader = csv.reader(csvFile, delimiter=";")
        row_index = 0
        for row in csv_reader:
            print("row index: " + str(row_index))
            if row_index < 5:
                nodes.append([])
                item_index = 0
                for item in row:
                    is_goal = row_index == GOAL_ROW and item_index == GOAL_COL
                    print(str(row_index) + "|" + str(item_index))
                    token = tokenDict[item]
                    nodes[row_index].append(Node(token, row_index, item_index, is_goal))
                    item_index += 1
            else:
                free_token = tokenDict[str(row[0])]
            row_index += 1
    return NodeSet(nodes), free_token
