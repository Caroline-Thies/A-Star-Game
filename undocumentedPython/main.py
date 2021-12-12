import InputReader
import AStar

INPUT_FILE_PATH = "Puzzle_6.CSV"
START_NODE_ROW = 4
START_NODE_COL = 1

GOAL_NODE_ROW = 0
GOAL_NODE_COL = 2


def print_path_edges(start_node, end_node):
    node = end_node
    reversed_edges = []
    while node.path_in_edge is not None:
        reversed_edges.append(node.path_in_edge)
        node = node.path_in_edge.source
    edges = reversed(reversed_edges)
    for edge in edges:
        print(edge)
        if not type(edge.movement) == type("  "):
            print(edge.dest.parent_set)
            print("new free token:")
            print(edge.dest.parent_set.free_token)


initial_nodeset = InputReader.get_nodeset_and_free_token_from_file(INPUT_FILE_PATH)

print("Read Input:")
print(str(initial_nodeset))
print("Free Token:")
print(str(initial_nodeset.free_token))
first_node = initial_nodeset.nodes[START_NODE_ROW][START_NODE_COL]
final_node = AStar.a_star(first_node)
print_path_edges(first_node, final_node)
