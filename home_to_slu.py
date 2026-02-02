from graph import Graph
import math

coords = {
    "APARTMENT": (0, 0),   
    "TELLEZ_INTERSECTION_1": (0, 150),
    "TELLEZ_INTERSECTION_2": (0, 300),
    "MAIN_ROAD_CORNER": (150, 300),
    "PACIFICO": (300, 300),  
    "ROAD_TO_CAMPUS_1": (300, 450),
    "ROAD_TO_CAMPUS_2": (450, 450),
    "CAMPUS_CROSSING": (600, 450),
    "SLU_GATE_SOUTH": (600, 550),
    "SLU_GATE_NORTH": (650, 650),
    "PARK_ROUTE": (450, 600),
    "ALT_RESIDENTIAL_ROUTE": (150, 450),
}

GOALS = ["SLU_GATE_SOUTH", "SLU_GATE_NORTH"]

def straight_line_to_nearest_gate(node_id: str) -> float:
    x, y = coords[node_id]
    best = float("inf")
    for g in GOALS:
        gx, gy = coords[g]
        d = math.hypot(x - gx, y - gy)
        if d < best:
            best = d
    return best

g = Graph()

g.add_node(
    "APARTMENT",
    [["TELLEZ_INTERSECTION_1", 150]],
    [straight_line_to_nearest_gate("APARTMENT")]
)

g.add_node(
    "TELLEZ_INTERSECTION_1",
    [["APARTMENT", 150],
     ["TELLEZ_INTERSECTION_2", 150],
     ["ALT_RESIDENTIAL_ROUTE", 320]],
    [straight_line_to_nearest_gate("TELLEZ_INTERSECTION_1")]
)

g.add_node(
    "TELLEZ_INTERSECTION_2",
    [["TELLEZ_INTERSECTION_1", 150],
     ["MAIN_ROAD_CORNER", 150]],
    [straight_line_to_nearest_gate("TELLEZ_INTERSECTION_2")]
)

g.add_node(
    "MAIN_ROAD_CORNER",
    [["TELLEZ_INTERSECTION_2", 150],
     ["PACIFICO", 150]],
    [straight_line_to_nearest_gate("MAIN_ROAD_CORNER")]
)

g.add_node(
    "PACIFICO",
    [["MAIN_ROAD_CORNER", 150],
     ["ROAD_TO_CAMPUS_1", 150]],
    [straight_line_to_nearest_gate("PACIFICO")]
)

g.add_node(
    "ROAD_TO_CAMPUS_1",
    [["PACIFICO", 150],
     ["ROAD_TO_CAMPUS_2", 150],
     ["ALT_RESIDENTIAL_ROUTE", 180]],
    [straight_line_to_nearest_gate("ROAD_TO_CAMPUS_1")]
)

g.add_node(
    "ROAD_TO_CAMPUS_2",
    [["ROAD_TO_CAMPUS_1", 150],
     ["CAMPUS_CROSSING", 150],
     ["PARK_ROUTE", 170]],
    [straight_line_to_nearest_gate("ROAD_TO_CAMPUS_2")]
)

g.add_node(
    "CAMPUS_CROSSING",
    [["ROAD_TO_CAMPUS_2", 150],
     ["SLU_GATE_SOUTH", 100],
     ["SLU_GATE_NORTH", 220]],
    [straight_line_to_nearest_gate("CAMPUS_CROSSING")]
)

g.add_node(
    "SLU_GATE_SOUTH",
    [["CAMPUS_CROSSING", 100]],
    [straight_line_to_nearest_gate("SLU_GATE_SOUTH")]
)

g.add_node(
    "SLU_GATE_NORTH",
    [["CAMPUS_CROSSING", 220],
     ["PARK_ROUTE", 230]],
    [straight_line_to_nearest_gate("SLU_GATE_NORTH")]
)

g.add_node(
    "PARK_ROUTE",
    [["ALT_RESIDENTIAL_ROUTE", 180],
     ["ROAD_TO_CAMPUS_2", 170],
     ["SLU_GATE_NORTH", 230]],
    [straight_line_to_nearest_gate("PARK_ROUTE")]
)

g.add_node(
    "ALT_RESIDENTIAL_ROUTE",
    [["TELLEZ_INTERSECTION_1", 320],
     ["ROAD_TO_CAMPUS_1", 180],
     ["PARK_ROUTE", 180]],
    [straight_line_to_nearest_gate("ALT_RESIDENTIAL_ROUTE")]
)

if __name__ == "__main__":
    start = "APARTMENT"
    goals = ["SLU_GATE_SOUTH", "SLU_GATE_NORTH"]

    ucs_result = g.ucs(start, goals)
    print("Uniform Cost Search (UCS):")
    print("  Cost:", ucs_result.cost)
    print("  Explored nodes:", ucs_result.explored_nodes)
    print("  Path:", [n.id for n in ucs_result.path])
    print("  Node details (g(n), h(n)):")
    g_accumulated = 0
    for i, node in enumerate(ucs_result.path):
        h_val = straight_line_to_nearest_gate(node.id)
        if i > 0:
            prev_node = ucs_result.path[i-1]
            g_accumulated += g.get_cost(prev_node.id, node.id)
        print(f"    {node.id}: g(n)={g_accumulated:.1f}, h(n)={h_val:.1f}")

    greedy_result = g.greedy(start, goals)
    print("\nGreedy Best-First Search:")
    print("  Cost:", greedy_result.cost)
    print("  Explored nodes:", greedy_result.explored_nodes)
    print("  Path:", [n.id for n in greedy_result.path])
    print("  Node details (g(n), h(n)):")
    g_accumulated = 0
    for i, node in enumerate(greedy_result.path):
        h_val = straight_line_to_nearest_gate(node.id)
        if i > 0:
            prev_node = greedy_result.path[i-1]
            g_accumulated += g.get_cost(prev_node.id, node.id)
        print(f"    {node.id}: g(n)={g_accumulated:.1f}, h(n)={h_val:.1f}")

    astar_result = g.astar(start, goals)
    print("\nA* Search:")
    print("  Cost:", astar_result.cost)
    print("  Explored nodes:", astar_result.explored_nodes)
    print("  Path:", [n.id for n in astar_result.path])
    print("  Node details (g(n), h(n)):")
    g_accumulated = 0
    for i, node in enumerate(astar_result.path):
        h_val = straight_line_to_nearest_gate(node.id)
        if i > 0:
            prev_node = astar_result.path[i-1]
            g_accumulated += g.get_cost(prev_node.id, node.id)
        print(f"    {node.id}: g(n)={g_accumulated:.1f}, h(n)={h_val:.1f}")