from typing import List

from Model import Node
from PriorityQueue import PriorityQueue


def a_star(start_node: Node):
    open_nodes = PriorityQueue()
    closed_nodes = []
    open_nodes.push(start_node)
    start_node.stepsToReach = 0
    while not open_nodes.is_empty():
        current_node: Node = open_nodes.pop()
        if current_node.get_is_valid_goal():
            return current_node
        closed_nodes.append(current_node)
        expand_node(current_node, open_nodes, closed_nodes)
    print("Something went wrong, could not find path")
    return None


def expand_node(current_node, open_nodes, closed_nodes):
    out_edges = current_node.get_edges()
    successor_nodes: List[Node] = [edge.dest for edge in out_edges]
    for i in range(len(successor_nodes)):
        successor_node = successor_nodes[i]
        if successor_node in closed_nodes:
            continue
        tentative_g = current_node.stepsToReach + 1
        if successor_node in open_nodes and tentative_g >= successor_node.stepsToReach:
            continue
        successor_node.update_steps_to_reach(tentative_g, out_edges[i])
        if successor_node not in open_nodes:
            open_nodes.push(successor_node)
