import sys


class DijkstraCalculator:
    def __init__(self, priority_implementation):
        self.priority_picker = priority_implementation

    def get_shortest_paths(self, nnodes, nodes, origin_node):
        visited_nodes = [False] * nnodes
        distance = [sys.float_info.max] * nnodes
        precs = [-1] * nnodes

        distance[origin_node] = 0
        self.priority_picker.append(0, nodes[origin_node], 0)
        while not self.priority_picker.empty():
            actual_permanent_node = self.priority_picker.pop(visited_nodes)
            if actual_permanent_node == -1:
                break
            visited_nodes[actual_permanent_node.index] = True
            for index in range(0, len(actual_permanent_node.neightboors)):
                arc_node = actual_permanent_node.neightboors[index]
                arc_cost = actual_permanent_node.costs[index]
                tentative = distance[actual_permanent_node.index] + arc_cost
                old_distance = distance[arc_node.index]
                if tentative < old_distance:
                    distance[arc_node.index] = tentative
                    precs[arc_node.index] = actual_permanent_node.index
                if not visited_nodes[arc_node.index]:
                    self.priority_picker.append(distance[arc_node.index], arc_node, old_distance)

        return precs, distance
