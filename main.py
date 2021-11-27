import InputReader
import AStar
# read input
from PriorityQueue import PriorityQueue

INPUT_FILE_PATH = "Puzzle_6.CSV"
START_NODE_ROW = 4
START_NODE_COL = 1

GOAL_NODE_ROW = 0
GOAL_NODE_COL = 2


def print_path_edges(start_node, end_node):
    node = end_node
    while node.path_in_edge is not None:
        print(node.path_in_edge)
        node = node.path_in_edge.source


initial_nodeset = InputReader.get_nodeset_and_free_token_from_file(INPUT_FILE_PATH)

# print("Read Input:")
# print(str(initial_nodeset))
# print("Free Token:")
# print(str(initial_nodeset.free_token))
first_node = initial_nodeset.nodes[START_NODE_ROW][START_NODE_COL]
# print("Start Node:\n" + str(first_node))
# give first node set to a*
final_node = AStar.a_star(first_node)
print_path_edges(first_node, final_node)
# for edge in edges_to_goal:
#    print(str(edge.movement))
# write output
