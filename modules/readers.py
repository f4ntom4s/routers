from modules.modelos import Node


class NodeReader:
    def read_nodes(self, nodes_file):
        file = open(nodes_file, "r")
        line = file.readline()
        return int(line)

    def read_arcs(self, nnodes, arcs_file):
        nodes = []
        for n in range(0, nnodes):
            nodes.append(Node(n + 1))
        file = open(arcs_file, "r")
        for line in file:
            if line == "EOF":
                break
            origin, destination, cost = line.split(" ")
            nodes[int(origin) - 1].add_arc(nodes[int(destination) - 1], int(cost))
        return nodes



