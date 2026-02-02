from graph import Graph
import math


coords = {
    "MADRID": (40.4168, -3.7038),
    "TOLEDO": (39.8628, -4.0273),
    "SEGOVIA": (40.9481, -4.1184),
    "AVILA": (40.6568, -4.6878),
    "CUENCA": (40.0705, -2.1376),
    "SALAMANCA": (40.9650, -5.6641),
    "CORDOBA": (37.8882, -4.7794),
    "VALENCIA": (39.4699, -0.3763),
}

GOALS = ["TOLEDO", "CORDOBA"]

AVERAGE_SPEED = 80  

def manhattan_distance(lat1, lon1, lat2, lon2):
    return abs(lat1 - lat2) + abs(lon1 - lon2) * 111 

def straight_line_to_nearest_goal(node_id: str) -> float:
    """Calculate estimated driving hours to nearest goal city using Haversine."""
    lat1, lon1 = coords[node_id]
    best = float("inf")
    for g in GOALS:
        lat2, lon2 = coords[g]
        dist_km = manhattan_distance(lat1, lon1, lat2, lon2)
        hours = dist_km / AVERAGE_SPEED
        if hours < best:
            best = hours
    return best

g = Graph()

g.add_node(
    "MADRID",
    [["TOLEDO", 1.0],
     ["SEGOVIA", 1.2],
     ["AVILA", 1.5],
     ["SALAMANCA", 2.5],
     ["CUENCA", 1.5],
     ["VALENCIA", 3.5],
     ["CORDOBA", 4.5]],
    [straight_line_to_nearest_goal("MADRID")]
)

g.add_node(
    "TOLEDO",
    [["MADRID", 1.0],
     ["CUENCA", 1.5],
     ["CORDOBA", 3.0]],
    [straight_line_to_nearest_goal("TOLEDO")]
)

g.add_node(
    "SEGOVIA",
    [["MADRID", 1.2],
     ["AVILA", 0.8],
     ["SALAMANCA", 1.5],
     ["CUENCA", 2.0]],
    [straight_line_to_nearest_goal("SEGOVIA")]
)

g.add_node(
    "AVILA",
    [["MADRID", 1.5],
     ["SEGOVIA", 0.8],
     ["SALAMANCA", 1.2]],
    [straight_line_to_nearest_goal("AVILA")]
)

g.add_node(
    "CUENCA",
    [["MADRID", 1.5],
     ["TOLEDO", 1.5],
     ["VALENCIA", 2.0],
     ["SEGOVIA", 2.0]],
    [straight_line_to_nearest_goal("CUENCA")]
)

g.add_node(
    "SALAMANCA",
    [["MADRID", 2.5],
     ["SEGOVIA", 1.5],
     ["AVILA", 1.2]],
    [straight_line_to_nearest_goal("SALAMANCA")]
)

g.add_node(
    "CORDOBA",
    [["MADRID", 4.5],
     ["TOLEDO", 3.0],
     ["VALENCIA", 4.0]],
    [straight_line_to_nearest_goal("CORDOBA")]
)

g.add_node(
    "VALENCIA",
    [["MADRID", 3.5],
     ["CUENCA", 2.0],
     ["CORDOBA", 4.0]],
    [straight_line_to_nearest_goal("VALENCIA")]
)

def generate_permutations(items):
    if len(items) <= 1:
        return [items]
    result = []
    for i in range(len(items)):
        remaining = items[:i] + items[i+1:]
        for perm in generate_permutations(remaining):
            result.append([items[i]] + perm)
    return result

def find_multi_goal_path(g, start, goals, algorithm):
    if len(goals) == 0:
        return None
    
    if len(goals) == 1:
        result = algorithm(start, goals)
        return result
    
    best_result = None
    best_cost = float('inf')
    
    for goal_order in generate_permutations(goals):
        current_start = start
        total_path = []
        total_cost = 0
        total_explored = 0
        
        for goal in goal_order:
            GOALS.clear()
            GOALS.append(goal)
            for city in coords.keys():
                h_val = straight_line_to_nearest_goal(city)
                g._Graph__heuristic[city] = [h_val]
            
            result = algorithm(current_start, [goal])
            
            if result.path is None or len(result.path) == 0:
                break
            
            path_nodes = [n.id for n in result.path]
            if total_path:
                total_path.extend(path_nodes[1:])
            else:
                total_path.extend(path_nodes)
            
            total_cost += result.cost
            total_explored += result.explored_nodes
            current_start = goal
        
        if total_cost < best_cost:
            best_cost = total_cost
            path_nodes_list = []
            for city in total_path:
                from node import Node
                path_nodes_list.append(Node(city))
            from searchpath import SearchPath
            best_result = SearchPath(path_nodes_list, total_cost, total_explored)
    
    GOALS.clear()
    GOALS.extend(goals)
    for city in coords.keys():
        h_val = straight_line_to_nearest_goal(city)
        g._Graph__heuristic[city] = [h_val]
    
    return best_result

if __name__ == "__main__":
    start = "MADRID"
    goals = ["TOLEDO", "CORDOBA"]

    print("SPAIN WEEKEND TRIP PLANNER")
    print("Finding optimal route from", start, "visiting all goals:", goals)
    
    ucs_result = find_multi_goal_path(g, start, goals, g.ucs)
    print("\nUniform Cost Search:")
    if ucs_result and ucs_result.path:
        print("Total Driving Time:", ucs_result.cost, "hours")
        print("Explored cities:", ucs_result.explored_nodes)
        print("Route:", ">".join([n.id for n in ucs_result.path]))
        

    greedy_result = find_multi_goal_path(g, start, goals, g.greedy)
    print("\nGreedy Best First Search:")
    if greedy_result and greedy_result.path:
        print("  Total Driving Time:", greedy_result.cost, "hours")
        print("  Explored cities:", greedy_result.explored_nodes)
        print("  Route:", ">".join([n.id for n in greedy_result.path]))
        

    astar_result = find_multi_goal_path(g, start, goals, g.astar)
    print("\nA* Search:")
    if astar_result and astar_result.path:
        print("  Total Driving Time:", astar_result.cost, "hours")
        print("  Explored cities:", astar_result.explored_nodes)
        print("  Route:", " >".join([n.id for n in astar_result.path]))
        
        
