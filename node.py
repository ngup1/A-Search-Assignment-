"""

The class Node is used by the classes List, Queue, Stack, Priority Queue, and Graph

- id is the node identifier
- parent is the parent's node id
- cost is the actual cost to reach the node from the initial state
- priority is used by the priority queue

"""

class Node:
    def __init__(self, id, parent=None, cost=0, priority=0):
        self.__id = id
        self.__parent = parent
        self.__cost = cost
        self.__priority = priority

    @property
    def id(self):
        return self.__id

    @property
    def parent(self):
        return self.__parent

    @property
    def cost(self):
        return self.__cost

    @property
    def priority(self):
        return self.__priority

    def __str__(self):
        return "'" + self.__id + "'" if self.__parent == None else "'" + self.__id + "', parent='" + str(self.__parent) + "', cost=" + str(self.__cost) + ", priority=" + str(self.__priority)