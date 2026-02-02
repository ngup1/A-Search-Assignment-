from node import *

"""

The class List is collection of nodes. Each node has the following attributes:

- id is the node identifier
- parent is the parent's node id
- cost is the actual cost to reach the node from the initial state
- priority is used by the priority queue

The interface of the class List provides the following functions:

- empty() returns true if the list is empty and false otherwise.
- add(node) adds the node at the rear of the list.
- remove() removes the node at the front of the list if the list is not empty.
- get(id) returns the node with the input id or None if the node is not in the list.
- contains(id) returns true if the node with the input id is in the list and false otherwise.
- size() returns the size of the list.

The class list is extended by subclasses Queue, Stack, and PriorityQueue. The attribute self._data is declared protected to let subclasses Stack and PriorityQueue access to it.

- Queue is an alias of the class List.
- Stack overrides the function add(node).
- PriorityQueue overrides the functions add(node) and remove().

"""

class List:
    def __init__(self):
        self._data = []

    def empty(self):
        return len(self._data) == 0

    def add(self, node):
        self._data.append(node)

    def remove(self):
        if not self.empty():
            return self._data.pop(0)

        return None

    def get(self, id):
        for node in self._data:
            if node.id == id:
                return node

        return None

    def contains(self, id):
        for node in self._data:
            if node.id == id:
                return True

        return False

    def size(self):
        return len(self._data)

    def __str__(self):
        list = "{ "

        for node in self._data:
            list = list + "[" + str(node) + "],"

        list = list[:-1] + " }"

        return list

# The subclass Queue

class Queue(List):
    pass

# The subclass Stack overrides the function remove()

class Stack(List):
    def remove(self):
        if not self.empty():
            return self._data.pop()

        return None

# The subclass PriorityQueue overrides the functions add(node), and remove()

class PriorityQueue(List):
    def add(self, node):
        super().add(node)

        p = self.size() - 1

        self.__shiftUp(p)

    def remove(self):
        if not self.empty():
            root_node = self._data[0]
            last_node = self._data.pop()

            if not self.empty():
                self._data[0] = last_node
                self.__shiftDown(0)

            return root_node

        return None

    def __swap(self, p, q):
        n = self._data[p]
        self._data[p] = self._data[q]
        self._data[q] = n

    def __shiftUp(self, child):
        parent = int((child - 1) / 2)

        if self._data[child].priority < self._data[parent].priority:
            self.__swap(parent, child)

            if parent != 0:
                self.__shiftUp(parent)

    def __shiftDown(self, parent):
        left_child = 2 * parent + 1
        right_child = 2 * parent + 2

        # the initial value for minimum is the index of the parent node

        minimum = parent

        # if the left child is within bounds and its priority is lower than minimum's priority, update minimum

        if left_child <= self.size() - 1 and self._data[left_child].priority < self._data[minimum].priority:
            minimum = left_child

        # if the right child is within bounds and its priority is lower than minimum's priority, update minimum

        if right_child <= self.size() - 1 and self._data[right_child].priority < self._data[minimum].priority:
            minimum = right_child

        # if minimum was updated and is not equal to parent, swap minimum and parent and recursively shift down the new minimum

        if minimum != parent:
            self.__swap(minimum, parent)
            self.__shiftDown(minimum)
            