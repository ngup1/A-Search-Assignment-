from list import *
from searchpath import *

"""

The class Graph is a weighted graph. It is implemented using a dictionary.

Nodes (vertices) are the keys of the dictionary and the list of adjacent nodes is the value associated to the key. The adjacency list cointains the node and the cost.
Heuristics are implemented with a list. Heuristics are used by Greedy Best-first search and A* search.

Graph = { node-1: [[node-1-1, cost-1-1], [node-1-2, cost-1-2] ... [node-1-m, cost-1-m]],
          node-2: [[node-2-1, cost-2-1], [node-2-2, cost-2-2] ... [node-2-m, cost-2-m]],
          ...
          node-n: [[node-n-1, cost-n-1], [node-n-2, cost-n-2] ... [node-n-m, cost-n-m]] }

heuristic = { node-1: [heuristic-1],
              node-2: [heuristic-2],
              ...
              node-n: [heuristic-n] }

The class Graph implements three search algorithms:

- Breadth-first search (BFS) uses a queue as frontier.
- Depth-first search (DFS) uses a stack as frontier.
- A* search uses a priority queue as frontier and uses the heuristic function f(n) = g(n) + h(n).
  The function f(n) combines the actual cost g(n) to reach node n from the initial state, and the heuristic h(n), which is the estimated cost to reach a goal from node n.

"""

class Graph:
    def __init__(self, graph=None, heuristic=None):
        self.__graph = {} if graph is None else graph
        self.__heuristic = {} if heuristic is None else heuristic

    def get_cost(self, source, destination):
        if source in self.__graph:
            for node in self.__graph[source]:
                if (node[0] == destination):
                    return node[1]

        return float('inf')

    def add_node(self, node, edges=None, heuristic=None):
        if node not in self.__graph:
            self.__graph[node] = [] if edges is None else edges
            self.__heuristic[node] = [0] if heuristic is None else heuristic

    def __str__(self):
        graph = "\n{"

        for node in self.__graph:
            graph = graph + "\n'" + node + "': " + str(self.__graph[node]) + ", "

        graph = graph[:-2] + "\n}"

        edges = "{"

        for node in self.__heuristic:
            edges = edges + "'" + node + "':" + str(self.__heuristic[node]) + ", "

        edges = edges[:-2] + "} \n"

        return graph + "\n" + edges if len(edges) > 1 else graph

    def __retrieve_search_path(self, initial, node, explored):
        path = []

        cost = 0

        while node.parent is not None:
            path.append(node)

            cost = cost + self.get_cost(node.parent, node.id)

            node = explored.get(node.parent)

        path.append(Node(initial))
        path.reverse()

        return SearchPath(path, cost, explored.size())




    # Breadth-first search (BFS) and Depth-first search (DFS)
    #
    # - BFS uses a Queue as frontier and expands the nodes to explore in natural order
    # - DFS uses a Stack as frontier and expands the nodes to explore in reversed order

    @staticmethod
    def __natural_order(list):
        return list

    @staticmethod
    def __reversed_order(list):
        return reversed(list)

    # The parameters of the function blind_search are the initial node, the list of goals, the frontier, and the function that returns the nodes to expand
    # The default search is Breadth-first search (BFS), since the frontier is a queue and the nodes are expanded in natural order

    def __blind_search(self, initial, goal, frontier=Queue(), expand_nodes=__natural_order):
        # initialize the list of explored nodes

        explored = List()

        # Breadth-first search (BFS) uses a queue as frontier, while Depth-first search (DFS) uses a stack

        frontier.add(Node(initial))

        while not frontier.empty():
            node = frontier.remove()

            if not explored.contains(node.id):
                explored.add(node)

                # if the goal state is found, return the search path

                if node.id in goal:
                    return self.__retrieve_search_path(initial, node, explored)

                # add successors to the frontier in natural order for BFS and in reverse order for DFS

                successors = expand_nodes(self.__graph[node.id])

                # successors is the adjacency list of the current node: [[node-1-1, cost-1-1], [node-1-2, cost-1-2] ... [node-1-m, cost-1-m]]

                for successor in successors:
                    # successor[0] is the node id, and successor[1] is the cost

                    successor_node = successor[0]
                    successor_cost = successor[1]

                    # add successor to the frontier if it has not been explored yet

                    if not explored.contains(successor_node):
                        frontier.add(Node(successor_node, node.id))

        # goal state not found

        return SearchPath()

    # Breadth-first search (BFS) and Depth-first search (DFS)

    def bfs(self, initial, goal):
        return self.__blind_search(initial, goal, Queue(), self.__natural_order)
    
    def dfs(self, initial, goal):
        return self.__blind_search(initial, goal, Stack(), self.__reversed_order)
    
        # A* search uses a heuristic function f(n) to choose the next node to explore
    #
    #    f(n) = g(n) + h(n)
    #
    # where:
    #
    #    g(n) is the actual cost to reach node n from the initial state
    #    h(n) is the estimated cost to reach a goal from node n
    #
    # Depending on the function f(n), A* search behaves as:
    #
    # - Uniform cost search      f(n) = g(n)
    # - Greedy Best-first search f(n) = h(n)
    # - A* search                f(n) = g(n) + h(n)

    @staticmethod
    def __uniform_cost(g, h):
        return g

    @staticmethod
    def __greedy(g, h):
        return h

    @staticmethod
    def __astar(g, h):
        return g + h

    def __astar_search(self, initial, goal, algorithm=__astar):
        # initialize the list of explored nodes

        explored = List()

        # A* search uses a priority queue as frontier

        frontier = PriorityQueue()
        
        # Calculate priority for initial node based on the algorithm
        g_initial = 0
        h_initial = int(self.__heuristic[initial][0])
        f_initial = algorithm(g_initial, h_initial)
        frontier.add(Node(initial, None, g_initial, f_initial))

        while not frontier.empty():
            node = frontier.remove()

            if not explored.contains(node.id):
                explored.add(node)

                # if the goal state is found, return the search path

                if node.id in goal:
                    return self.__retrieve_search_path(initial, node, explored)

                # add successors to the frontier

                successors = self.__graph[node.id]

                # successors is the adjacency list of the current node: [[node-1-1, cost-1-1], [node-1-2, cost-1-2] ... [node-1-m, cost-1-m]]

                for successor in successors:
                    # successor[0] is the node id, and successor[1] is the cost

                    successor_node = successor[0]
                    successor_cost = successor[1]

                    # add successor to the frontier if it has not been explored yet

                    if not explored.contains(successor_node):

                        # g(n) represents the actual cost to reach the node from the initial state

                        g = int(node.cost + successor_cost)

                        # h(n) represents the estimated cost to reach a goal state from node n

                        h = int(self.__heuristic[successor_node][0])

                        # f(n) is determined by the algorithm: Uniform cost search uses g(n), Greedy Best-first search uses h(n), and A* search uses g(n) + f(n)

                        f = algorithm(g, h)

                        frontier.add(Node(successor_node, node.id, g, f))

        # goal state not found

        return SearchPath()

    # A* search behaves as Uniform cost search, Greedy Best-first search, or A*

    def ucs(self, initial, goal):
        return self.__astar_search(initial, goal, self.__uniform_cost)

    def greedy(self, initial, goal):
        return self.__astar_search(initial, goal, self.__greedy)

    def astar(self, initial, goal):
        return self.__astar_search(initial, goal, self.__astar)
