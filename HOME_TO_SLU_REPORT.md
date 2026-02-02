# A* Search Algorithm Analysis Report

## Problem Description

For this assignment, I implemented A* search, USC, and Greedy Best First Search to solve a real-world pathfinding problem. The problem is about finding the best route from my apartment in Pacifico to the SLU campus Guzman El Bueno metro gates. I modeled this as a graph search problem where we start at the APARTMENT and need to reach either SLU_GATE_SOUTH  or SLU_GATE_NORTH, representing the two Guzman El Bueno metro gates. The graph I created has 12 different nodes that represent intersections and landmarks around Madrid on the way to campus. Each connection between nodes has a cost that represents the actual distance you'd travel. These costs range from 100 to 320 units. I used a straight-line distance heuristic method, which calculates how far each node is from the nearest goal state using the Euclidean distance formula. So for any node h(n) is the minimum of the distance to SLU_GATE_SOUTH or SLU_GATE_NORTH. This heuristic is admissible because it never overestimates the true cos because the straight-line distance is always less than or equal to the actual path you'd have to take.

## Computed Values: Actual Costs and h(n)

I ran all three algorithms and they all converged on the same path in the end, which was interesting. The path goes APARTMENT → TELLEZ_INTERSECTION_1 → ALT_RESIDENTIAL_ROUTE → PARK_ROUTE → SLU_GATE_NORTH, with a total cost of 880.

- For Uniform Cost Search, it explored 10 nodes total. Looking at the actual costs and heuristic values along the path: starting at APARTMENT, g(n) is 0 and h(n) is 813.9. Then at TELLEZ_INTERSECTION_1, the actual cost g(n) is 150 (since we traveled 150 units) and h(n) is 721.1. At ALT_RESIDENTIAL_ROUTE, g(n) is 470 and h(n) drops to 461.0, which makes sense because we're getting closer. PARK_ROUTE has g(n) of 650 and h(n) of 158.1, and finally at SLU_GATE_NORTH, g(n) is 880 (the total path cost) and h(n) is 0 since we reached the goal. UCS only uses g(n) for its search, so it doesn't care about the heuristic values.

- Greedy Best-First Search found the exact same path but only explored 5 nodes, which is way more efficient. The g(n) and h(n) values are the same as UCS since it's the same path, but Greedy only uses h(n) for its priority function. So it's basically just following whatever looks closest to the goal at each step, ignoring how much it actually costs to get there.

- A* Search also found the same path and explored 5 nodes like Greedy. A* uses both g(n) and h(n) combined, so its priority function is f(n) = g(n) + h(n). At APARTMENT, f(n) would be 0 + 813.9 = 813.9. At TELLEZ_INTERSECTION_1, it's 150 + 721.1 = 871.1. The values go up and down as we progress, but A* balances both the actual cost and the estimated remaining cost.

## Comparative Analysis

All three algorithms found the same optimal path with a cost of 880. I think the convergance of paths could be caused by the nodes I chose all going in the same direction. It makes it much simpler in all cases to just pick the cheaper one, and you end up gatehring the best path. Some cases just visit more or less nodes to find the path. You can make it more complex by adding more nodes in different directions. 

 UCS is found the optimal path because it explored nodes in order of increasing actual cost, so it will always find the shortest path eventually especially if the optioins are narrow. A* also guarantees the best solutoin as long as the heuristic is admissible, which mine is. Greedy Best-First Search doesn't guarantee optimality, but in this case it happened to find the optimal path anyway because there were minimal choices to make. There was still a big difference in efficiency. UCS explored 10 nodes while both Greedy and A* only explored 5 nodes. That means Greedy and A* were twice as efficient in terms of how many nodes they had to check. This makes sense because the heuristic helps them avoid exploring paths that don't look promising. For example, when the algorithm is at TELLEZ_INTERSECTION_1, the heuristic shows that ALT_RESIDENTIAL_ROUTE (h=461.0) is closer to the goal than continuing along the main road path. So Greedy and A* can skip exploring all those intermediate nodes like TELLEZ_INTERSECTION_2, MAIN_ROAD_CORNER, PACIFICO, etc. UCS doesn't have this ablity and has to explore systematically based only on actual cost, so it checks more nodes before figuring out which path is best.

## Conclusions

For this specific problem and based on the nodes given to the search algorithm, A* and Greedy were both twice as efficient as UCS in terms of nodes explored. The straight-line distance heuristic worked really well because it gave good guidance about which direction to go. I think A* would be the best choice for most real applications because you get both optimality and efficiency. UCS and GBFS would struggle more given more nodes because they might begin exploring in the wrong direction or other sub optimal paths. 


