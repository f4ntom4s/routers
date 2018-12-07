import sys


class BucketNodePriorityQueue:
    def __init__(self):
        self.buckets = [[]]
        self.current = 0

    def append(self, distance, node, old_distance):
        if old_distance < len(self.buckets) and old_distance != distance:
            i = 0
            bucket_length = len(self.buckets[old_distance])
            while i < bucket_length:
                if self.buckets[old_distance][i] == node:
                    self.buckets[old_distance].pop(i)
                    bucket_length -= 1
                else:
                    i += 1

        if distance > len(self.buckets):
            self.buckets.extend([[]] * (distance - len(self.buckets) + 1))
        self.buckets[distance].append(node)

    def pop(self, visited):
        self.find_next_bucket()
        while not self.empty():
            while len(self.buckets[self.current]) != 0:
                first_element = self.buckets[self.current].pop()
                if not visited[first_element.index]:
                    return first_element
            self.find_next_bucket()
        return -1

    def empty(self):
        if self.current == len(self.buckets):
            return True
        if len(self.buckets[self.current]):
            return False
        self.find_next_bucket()
        if self.current == len(self.buckets):
            return True
        return False

    def find_next_bucket(self):
        for i in range(self.current, len(self.buckets)):
            if len(self.buckets[i]):
                self.current = i
                return
        self.current = len(self.buckets)
        return


class NodePriorityQueue:
    def __init__(self):
        self.queue = []

    def append(self, distance, node, old_distance):
        self.queue.append([distance, node])

    def pop(self, visited):
        if len(self.queue) == 0:
            return -1
        min_index = 0
        queue_len = len(self.queue)
        i = 0

        while i < queue_len:
            if visited[self.queue[i][1].index]:
                self.queue.pop(i)
                queue_len = len(self.queue)
                if queue_len == 0:
                    return -1
            else:
                if self.queue[i][0] < self.queue[min_index][0]:
                    min_index = i
                i += 1
        pair = self.queue.pop(min_index)
        node = pair[1]
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
        self.index = label - 1

    def __str__(self):
        return str(self.label)

    def add_arc(self, destination, cost):
        self.neightboors.append(destination)
        self.costs.append(cost)


