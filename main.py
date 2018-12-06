import sys
import time

from modules.dijkstra import DijkstraCalculator
from modules.modelos import BucketNodePriorityQueue, NodePriorityQueue
from modules.readers import NodeReader


def run_single_instance(nodes_file, arcs_file, origin_index):
    reader = NodeReader()
    nnodes = reader.read_nodes(nodes_file)
    nodes = reader.read_arcs(nnodes, arcs_file)

    max_arc = 0
    for node in nodes:
        for index in range(len(node.neightboors)):
            if node.costs[index] > max_arc:
                max_arc = node.costs[index]


    print(max_arc)
    calculator = DijkstraCalculator(NodePriorityQueue())  # classic implementation
    calculator2 = DijkstraCalculator(BucketNodePriorityQueue(max_arc))  # Dials implementation




    start_time = time.time()
    precs, distance = calculator.get_shortest_paths(nnodes, nodes, origin)
    print("Classic time: --- %s seconds ---" % (time.time() - start_time))
    print(precs)
    print(distance)
    start_time = time.time()
    precs2, distance2 = calculator2.get_shortest_paths(nnodes, nodes, origin_index)
    print("Dials implementation's time--- %s seconds ---" % (time.time() - start_time))
    print(precs2)
    print(distance2)
    if precs != precs2:
        print("solutions are note equal")
    if distance != distance2:
        print("solutions are note equal")



nodes_file = sys.argv[1]
arcs_file = sys.argv[2]
origin = int(sys.argv[3]) - 1

run_single_instance(nodes_file, arcs_file, origin)

#print(nodes)


