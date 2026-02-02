"""

The class SearchPath is used by the class Graph.

A SearchPath object is used to return the solution to a search problem. When path is None there is no solution, otherwise the solution is given by path, cost and explored nodes

"""

class SearchPath:
    def __init__(self, path=None, cost=None, explored_nodes=None):
        self.__path = path
        self.__cost = cost
        self.__explored_nodes = explored_nodes

    @property
    def path(self):
        return self.__path

    @property
    def cost(self):
        return self.__cost

    @property
    def explored_nodes(self):
        return self.__explored_nodes