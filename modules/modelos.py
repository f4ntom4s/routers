import sys


class BucketNodePriorityQueue:
    def __init__(self, max_diff):
        self.buckets = [[]] * (max_diff + 1)
        self.min_bucket = sys.float_info.max

    def append(self, distance, node):
        #check if element exist in bucket
        for elem in self.buckets[distance]:
            if elem.label == node.label:
                return

        self.buckets[distance].append(node)
        if self.min_bucket > distance:
            self.min_bucket = distance

    def pop(self, visited):
        while len(self.buckets[self.min_bucket]):
            first_element = self.buckets[self.min_bucket].pop(0)
            if not visited[first_element.index]:
                return first_element
        self.find_next_bucket()
        return self.buckets[self.min_bucket].pop(0)

    def empty(self):
        #print([x.label for x in self.buckets[35]])
        if self.min_bucket >= sys.float_info.max:
            return True
        if len(self.buckets[self.min_bucket]):
            return False
        self.find_next_bucket()
        if self.min_bucket >= sys.float_info.max:
            return True
        return False

    def find_next_bucket(self):
        for i in range(self.min_bucket, len(self.buckets)):
            if len(self.buckets[i]):
                self.min_bucket = i
                return
        self.min_bucket = sys.float_info.max
        return


class NodePriorityQueue:
    def __init__(self):
        self.queue = []

    def append(self, distance, node):
        self.queue.append([distance, node])

    def pop(self, visited):
        if len(self.queue) == 0:
            return -1
        min_index = 0
        queue_len = len(self.queue)
        i = 0

        print([x[1].label for x in self.queue])
        while i < queue_len - 1:
            if self.queue[i][0] < self.queue[min_index][0] and not visited[self.queue[i][1].index]:
                min_index = i

            if visited[self.queue[i][1].index]:
                del self.queue[i]
                queue_len -= 1
            else:
                i += 1

        node = self.queue[min_index][1]
        del self.queue[min_index]
        return node

    def empty(self):
        if len(self.queue) == 0:
            return True
        return False


class Node:
    def __init__(self, label):
        self.label = label
        self.neightboors = []
        self.costs = []
        self.nearest = -1
        self.nearest_distance = sys.float_info.max
        self.index = label - 1

    def __str__(self):
        return str(self.label)

    def add_arc(self, destination, cost):
        self.neightboors.append(destination)
        self.costs.append(cost)

        if cost < self.nearest_distance:
            self.nearest_distance = cost
            self.nearest = destination

