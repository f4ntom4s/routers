import sys


class DijkstraCalculator:
    def __init__(self, priority_implementation):
        self.priority_picker = priority_implementation

    def get_shortest_paths(self, nnodes, nodes, origin_node):
        visited_nodes = [False] * nnodes
        distance = [sys.float_info.max] * nnodes
        precs = [-1] * nnodes

        distance[origin_node] = 0
        self.priority_picker.append(0, nodes[origin_node])
        while not self.priority_picker.empty():
            actual_node = self.priority_picker.pop(visited_nodes)
            if not actual_node:
                break
            visited_nodes[actual_node.index] = True

            for index in range(len(actual_node.neightboors)):
                arc_node = actual_node.neightboors[index]
                arc_cost = actual_node.costs[index]
                tentative = distance[actual_node.index] + arc_cost
                #print(tentative)
                if tentative < distance[arc_node.index]:
                    distance[arc_node.index] = tentative
                    precs[arc_node.index] = actual_node.index
                if not visited_nodes[arc_node.index]:
                    self.priority_picker.append(arc_cost, arc_node)

        return precs, distance
